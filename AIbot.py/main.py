import openai
import requests
from colored import fg, bg, attr

# Set the API key
openai.api_key = ""


while True:
    # Ask the user for input
    prompt = input("Enter a description of the image you want to generate: ")

    # Use the DALL-E API to generate an image
    image_url = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )["data"][0]["url"]

    # Download the image
    image_data = requests.get(image_url).content

    # Save the image to a file
    with open("image.jpg", "wb") as f:
        f.write(image_data)

    # Print a message to confirm that the image has been generated
    print("Image generated and saved to 'image.jpg'")

    print(fg("green") + "Please consider donating to my Ethereum address :) " + attr("reset"))
    print(fg("cyan") + "  0x81f7e0c3b6f05eb76f98c2eb32b16ea5327165eb" + attr("reset"))
    print(fg("yellow") + "  The network is ERC20! If you don't see this message, then remove the last 4 lines from the code." + attr("reset"))
    print(fg("blue") + "  I love money just like you! " + "\u2764" + attr("reset"))
