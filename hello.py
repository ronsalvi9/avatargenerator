import python_avatars as pa
from python_avatars import clothing_types

# Completely random avatar
random_avatar_1 = pa.Avatar.random()

# Fixed avatar but random clothes

random_avatar_2 = pa.Avatar(
    style=pa.AvatarStyle.CIRCLE,
    hair_color=pa.HairColor.BLACK,
    accessory=pa.AccessoryType.NONE,
    clothing=pa.ClothingType.pick_random(),  # The clothes are chosen randomly
)


# random_avatar_1.render('Random.svg')
random_avatar_2.render('RandomClothes.svg')
