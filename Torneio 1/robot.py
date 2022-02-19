def robot(comandos):
    rect = []
    mx, my, Mx, My, x, y = 0,0,0,0,0,0
    dx,dy = 0,1
    for c in comandos:
        if c == 'H':
            rect.append( (mx,my,Mx,My) )
            mx, my, Mx, My, x, y, dx, dy = 0,0,0,0,0,0,0,1
        elif c == 'A':
            x += 1*dx
            y += 1*dy
            mx = min(x,mx)
            Mx = max(x,Mx)
            my = min(y,my)
            My = max(y,My)
        elif c == 'E':
            dx,dy = -dy,dx
        elif c == 'D':
            dx,dy = dy,-dx
    return rect
