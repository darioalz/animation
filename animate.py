'''
Widget animation
================

This example demonstrates creating and applying a multi-part animation to
a button widget. You should see a button labelled 'plop' that will move with
an animation when clicked.
'''

import kivy
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button

import pygame
import time
import random

pygame.mixer.init()
pygame.mixer.music.load("[Lanota] WAiKURO - Androgynos (Full Version).mp3")


start=0
end=0

class TestApp(App):

    def animate(self, instance):
        start = time.time()
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        animation = Animation(pos=(random.randint(0,700), random.randint(0,550)), t='out_bounce')
        
        animation &= Animation(size=(100, 50))
        

        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        animation.start(instance)

    def build(self):
        # create a button, and  attach animate() method as a on_press handler
        
        button = Button(size_hint=(None, None), text='plop',
                        on_press=self.animate)
        
        end = time.time()
        
        print(end-start)
        return button

    def button2_click():
        build.invoke


if __name__ == '__main__':
    TestApp().run()
        
    
    
