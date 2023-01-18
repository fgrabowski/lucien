import board
import neopixel
import asyncio

# Pixels
total_pixels = 276
# one stripe has 46 pixels, 92 equals whole shelf == 2 strips.
shelf_length = 46
# Multiplies dots by 10, this means the animation strip length is 10 leds
animation_length = 10

pixels = neopixel.NeoPixel(board.GP28, total_pixels, brightness=0.2, auto_write=False)


# shelf_number means which shelf is chosen
def animation(shelf_number):
    # 0 | 0x46 - 0+1 x 46 0+2x46 - 1x46 92-i 0+i
    while True:
        # First index of 1st led stripe on shelf
        start_anim = shelf_number * shelf_length
        # Last index of 2nd led stripe on shelf
        stop_anim = (shelf_number + 2) * shelf_length
        #
        for i in range(shelf_length):
            for j in range(animation_length):
                offset = (i + j) % shelf_length
                pixels[start_anim + offset] = [0, 10, 0]
                pixels[stop_anim - 1 - offset] = [10, 0, 0]
            pixels.show()

            # Sleep time, means how fast animation is supposed to be
            await asyncio.sleep(0.08)

            # Multiplies deleting dots by 10
            for j in range(animation_length):
                offset = (i + j) % shelf_length
                pixels[start_anim + offset] = [0, 0, 0]
                pixels[stop_anim - 1 - offset] = [0, 0, 0]
            pixels.show()


async def main():
    # executes animation and has which shelf as an argument
    animation_as = asyncio.create_task(animation(0))
    await asyncio.gather(animation_as)


asyncio.run(main())
