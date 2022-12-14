import os
import mujoco_py as mp
from pathlib import Path

from gym_grasper.controller.MujocoController import MJ_Controller

path = os.path.realpath(__file__)
path = str(Path(path).parent)
model = mp.load_model_from_path(path + "\\UR5+gripper\\UR5gripper_2_finger_example.xml")

# create controller instance
controller = MJ_Controller(model=model)

# Display robot information
controller.show_model_info()

# Wait a second
controller.stay(1000)

# Move ee to position above the object, plot the trajectory to an image file, show a marker at the target location
controller.move_ee([0.0, -0.6, 1.0], plot=True, marker=True)
# controller.move_ee([0.0, 0.0, 0.0], plot=True, marker=True)
controller.stay(1000)

# Move down to object
controller.move_ee([0.0, -0.6, 0.895])

# Wait a second
controller.stay(1000)

# Attempt grasp
controller.grasp()

# Move up again
controller.move_ee([0.0, -0.6, 1.0])

# Throw the object away
controller.toss_it_from_the_ellbow()

# Wait before finishing
controller.stay(2000)
