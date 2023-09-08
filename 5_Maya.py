"""
Задание 5 [Maya]
Имеется некая геометрическая поверхность в сцене. 
Вам необходимо написать скрипт, который расположит другие выделенные объекты (сферы или локаторы, неважно) 
на поверхности текущего объекта в рандомных позициях. Используйте любой известный вам метод. 
Если объекты при расположении на поверхности будут пересекаться с поверхностью - это нормально, 
т.к. пивоты объектов обычно находятся в центре их геометрии. 
Иные способы расположения будет намного труднее реализовать, так что делать этого не надо.
"""

import random
import maya.cmds as cmds

def place_objects_on_surface(object_count, surface):
    # Получаем геометрию поверхности
    faces = cmds.ls(surface + '.f[*]', fl=True)
    
    # Выбираем случайные полигоны на поверхности
    selected_faces = random.sample(faces, object_count)
    
    for face in selected_faces:
        # Получаем случайную точку на поверхности полигона
             
        u, v = random.uniform(0, 1), random.uniform(0, 1)
        point = cmds.pointOnSurface(face, u=u, v=v, position=True, ch=False)
        
        # Создаем сферу на поверхности в полученной точке
        sphere = cmds.polySphere(radius=100)[0]
        cmds.move(point[0], point[1], point[2], sphere, absolute=True)

object_count = 300
surface = "pSphere1"

place_objects_on_surface(object_count, surface)
