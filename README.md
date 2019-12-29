# pixel2discord https://discord.gg/MJ6kdjH
Convert pixel art to massive Discord messages w/ emojis

* For python 2.7 might work with python 3
* Requires PIL (Recomends using pillow)

* User changable variables:
```python
alpha = False		# Alpha for each pixel (Fully transparent pixels ignore this)
filename = 'user1.png'	# File name
```

## print_emojis.ahk
* Requires [`AutoHotKey`](https://www.autohotkey.com/ "AutoHotKey Website") installed
* Needs to be in the same directory as disp.txt. 
* Will start 'printing' after 5s with 1s between each line so make sure to have the discord textbox selected within 5s of starting it.


## "Instructions"
* Suggested: Change the `filename` variable to filename of the file you want to convert (I might add a file picker later)
* Optional: Change the `alpha` variable from `False` to `True` in `convert.py` to enable partial transparency (Only lightly tested)
* Run `convert.py`
* Once it is done generating files in the subfolder of it's current directory with the name of the original file appended with `_out`, add them to a Discord Guild and don't change the names.
* Optional: Put `print_emojis.ahk` in the newly created directory with the newly created `disp.txt` file have Discord open in the channel you want to print the image to, run it and click the Discord text box after 5s it should start printing


## Examples
![Me](https://cdn.discordapp.com/attachments/594881843501727755/660034582157983793/unknown.png "Me")

![Sans](https://media.discordapp.net/attachments/653083168030851102/660671611669839882/unknown.png "Sans")

![Baba](https://media.discordapp.net/attachments/594881843501727755/660558362089488416/unknown.png "Baba")

![Violet](https://media.discordapp.net/attachments/653083168030851102/660673071379906560/unknown.png "Violet")

