from variables import Variables

vars = Variables()  # Variable Holster Object

while not vars.done:  # Loop to render each frame
    vars.doAnUpdate()  # Main function that collects event data, and paints the current frame to the screen