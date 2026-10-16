# 1) Считывание ввода
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return None
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            crosshair.hit_sound.play()