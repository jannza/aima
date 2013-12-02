# -*- coding: utf-8 -*-
from probability import *


#a)lisada võrku Boole' muutujad IcyWeather ja StarterMotorMootor
#b)lisada tingimuslikud tõenäosustabelid kõikidele tippudele
#c)Kui palju on sõltumatud selles võrgus?
#d)Pakkuda välja 3 erinevat mõistlikut päringut.
#Arvutdada välja erinevate lähenemistega EnumAsk, EliminationAsk abil ja LW ja MCMC abil
#Võrrelda tulemusi mitu iteratsiooni


#define true false
T, F = True, False




starting = BayesNet([
    ('IcyWeather', '', 0.3),                 
    ('Battery', 'IcyWeather', {T: 0.7, F: 0.9}),
    ('Radio', 'Battery', {T: 0.8, F: 0.2}),
    ('Ignition', 'Battery',{T: 0.95, F: 0.05}),
    ('Gas', '', 0.8),
    ('StarterMotor','Ignition', {T: 0.9, F: 0.1}),
    ('Starts', 'StarterMotor Gas', 
        {(T, T): 0.99, (T, F): 0.005, (F, T): 0.005, (F, F): 0}),
    ('Moves', 'Starts', {T: 0.95, F: 0.05})
    ])



#Think of good example queries

samples = [50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]



#first
#its cold outside, but radio plays, will the igntion turn on?
print(enumeration_ask('Ignition', dict(IcyWeather=T, Radio=T), starting).show_approx())
 
 
for elem in samples:
    print("Testing with "+str(elem)+" samples")
    print(likelihood_weighting('Ignition', dict(IcyWeather=T, Radio=T), starting, elem).show_approx())
    print(gibbs_ask('Ignition', dict(IcyWeather=T, Radio=T), starting, elem).show_approx())


#second
#There's gas in the tank, Ignition is on, will the car move?
print(enumeration_ask('Moves', dict(Ignoition=T, Gas=T), starting).show_approx())
 
 
for elem in samples:
    print("Testing with "+str(elem)+" samples")
    print(likelihood_weighting('Moves', dict(Ignoition=T, Gas=T), starting, elem).show_approx())
    print(gibbs_ask('Moves', dict(Ignoition=T, Gas=T), starting, elem).show_approx())



#third
#Theres no minus degrees outside, and radio doesn't work, will the engine start?
print(enumeration_ask('Starts', dict(Radio=F, IcyWeather=F), starting).show_approx())
 
for elem in samples:
    print("Testing with "+str(elem)+" samples")
    print(likelihood_weighting('Starts', dict(Radio=F, IcyWeather=F), starting, elem).show_approx())
    print(gibbs_ask('Starts', dict(Radio=F, IcyWeather=F), starting, elem).show_approx())

