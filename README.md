# bot.py

Install - Dependencies:
`pip install termcolor pyHM`

### Features

- #### Colorful prints:
    ```python
    import bot
  
    print(bot.error, "Error message")
    print(bot.warn, "Warning message")
    print(bot.info, "Info message")
    ```
  
- #### Mouse position:
    ```python
    import bot
  
    print(bot.mouse_position())
    ```
    `[1203, 719]`

- #### Mouse move:
    Move the cursor to some random position in the rectangle (x,y,w,h)
    
    ```python
    import bot
  
    bot.mouse_move(100,100,10,10, click="left", debug=True)
    ```
    Usage: `bot.mouse_move(x, y, w, h, [click], [debug], [movSpeed])`  
      
    #### Optionals:  
    "click": str, should be "left", "right", "double" or "none", default "none"  
    "movSpeed": float, the higher movSpeed slower mouse speed, default 1  
    "debug": bool, prints where mouse will go, default False  
  

    
