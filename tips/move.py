def keyboard():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        rect_1.x += 5
    if keys[pygame.K_w]:
        rect_1.y -= 5
    if keys[pygame.K_s]:
        rect_1.y += 5
    if keys[pygame.K_a]:
        rect_1.x -= 5



rect.center = pygame.mouse.get_pos()