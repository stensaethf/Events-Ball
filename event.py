# sampleevent.py
# A Python module to bounce a ball around a window
# Created by Frederik Roenn Stensaeth and Javier Moran
# 03.03.14

# Import libraries
import sys
import pygame
from pygame.locals import *


# Define main function. Takes no parameters. Sets up graphic screen with ball,
#and allows for user input.
def main():


   # Intiniating pygame
   pygame.init()
   # Set width and height
   width, height = 475, 333
   # Create tuple with width and height
   size = (width, height)
   # List to set speed
   speed = [2, 2]
   # Load image.jpg and store as background
   background = pygame.image.load("image.jpg")
   # Get rectangular area of background image
   background_image = background.get_rect()
   # Set size of graphics window to size
   screen = pygame.display.set_mode(size)
   # Load ball.gif and store as ball
   ball = pygame.image.load("ball.gif")
   # Get rectangular ear of ball image
   ballrect = ball.get_rect()

   # Set up infinate loop
   while True:
      # Loop over events in event list
      for event in pygame.event.get():
         # Check if event is QUIT, if so, exit
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         # Check if event is a pressed key
         elif event.type == KEYDOWN:
            # If pressed key is 'q' exit
            if event.key == K_q:
               pygame.quit()
               sys.exit()
            # If pressed key is arrow left, subtract one from the horizontal 
            #speed of the ball
            elif event.key == K_LEFT:
               speed[0] -= 1
            # If pressed key is 'c', reverse direcion of ball
            elif event.key == K_c:
               speed[0] *= -1
               speed[1] *= -1
            # If pressed key is arrow right, add one to the horizontal speed
            #of the ball 
            elif event.key == K_RIGHT:
               speed[0] += 1
            # If pressed key is arrow up, subtract one from the vertical speed
            #of the ball
            elif event.key == K_UP:
               speed[1] -= 1
            # If pressed key is arrow down, add one to the vertical speeed of
            #the ball
            elif event.key == K_DOWN:
               speed[1] += 1
         # Check if event is mouse click
         elif event.type == MOUSEBUTTONDOWN:
            # Get position of mouse click
            x, y = pygame.mouse.get_pos()
            # Get coordinates of ball
            a, s, w, l = ballrect
            # If ball was clicked, print message
            if a <= x <= (a + w) and s <= y <= (y + l):
               print "The ball has been clicked!"
            # If ball was not clicked, print message
            else:
               print "The ball was not clicked!"
      
      # Move ball according to speed
      ballrect = ballrect.move(speed)
      # If ball hits left or right edge of graphics window, reverse horizontal
      #speed
      if ballrect.left < 0 or ballrect.right > width:
         speed[0] = -speed[0]
      # If ball hits top or bottom edge of graphics window, reverse vertical
      #speed
      if ballrect.top < 0 or ballrect.bottom > height:
         speed[1] = -speed[1]

      # Redraw background pixels that were altered earlier
      screen.blit(background, background_image)
      # Draw new ball
      screen.blit(ball, ballrect)
      # Display new image
      pygame.display.flip()


if __name__ == '__main__':
   main()
