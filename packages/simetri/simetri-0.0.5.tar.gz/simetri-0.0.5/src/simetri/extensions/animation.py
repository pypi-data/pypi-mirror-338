from dataclasses import dataclass
from types import MethodType

from simetri.canvas.canvas import Canvas


@dataclass
class Prop:
    '''A Shape or Batch item that will be animated.
        Any attribute of the Prop can be animated.
        update_func is called with (item, frame, **kwargs) and should
        update the item.
        Args:
            item (object): The item to be animated.
            update_func (callable): The function that updates the item.
            start (int): The start frame.
            end (int): The end frame.

    '''
    item: object
    update_func: callable = None
    start: int = 0
    end: int = 1e6
    visible_func: callable = None

    def next(self, frame, **kwargs):
        '''Updates the item to the next frame.
            Args:
                frame (int): The current frame.
                **kwargs: Additional keyword arguments.

            Returns: self.update_func(item, frame, **kwargs)
        '''
        return self.update_func(self.item, frame, **kwargs)


    def visible(self, frame, **kwargs):
        '''Updates the item to the next frame.
            Args:
                frame (int): The current frame.
                **kwargs: Additional keyword arguments.

            Returns: self.update_func(item, frame, **kwargs)
        '''
        if self.visible_func:
            return self.visible_func(self.item, frame, **kwargs)

        return True

@dataclass
class Animation:
    '''A class to represent an animation.
        Args:

            duration (int): The duration of the animation in frames.
            frame_rate (int): The number of frames per second.

        Attributes:
            name (str): The name of the animation.
            frames (list): A list of frames.
            currentFrame (int): The current frame.
            currentTime (float): The current time. [s]
            frame_rate (int): The number of frames per second. [fps]

        Methods:
            update: Updates the animation.
            getCurrentFrame: Returns the current frame.
            reset: Resets the animation.
            isFinished: Returns True if the animation is finished.
            __str__: Returns the name of the animation and the current frame.

        Returns:
            Animation: An animation object.
    '''

    props: list
    duration: int
    frame_rate: int = 30

    def __post_init__(self):
        self.currentFrame = 0
        self.currentTime = 0
        self.frameTime = 1 / self.frame_rate
        self.props = self.props or []


    def __str__(self):
        return self.name + " " + str(self.currentFrame) + "/" + str(len(self.frames))

    def update(self, dt):
        self.currentTime += dt
        if self.currentTime >= self.frameTime:
            self.currentTime = 0
            self.currentFrame += 1
            if self.currentFrame >= len(self.frames):
                self.currentFrame = 0

    def getCurrentFrame(self):
        return self.frames[self.currentFrame]

    def reset(self):
        self.currentFrame = 0
        self.currentTime = 0

    def isFinished(self):
        return self.currentFrame == len(self.frames) - 1

    def render(self, directory, file_name, limits=None):
        '''Renders the animation.
            Args:
                directory (str): The directory to save the animation.
                file_name (str): The name of the file.
                limits (tuple): The limits of the canvas. xmin, xmax, ymin, ymax.
        '''
        for t in range(self.duration):
            if t > 0:
                for prop in [x for x in self.props if x.start <= t <= x.end]:
                    prop.next(t)
                canvas = Canvas()
                if limits:
                    canvas.limits = limits
                for prop in self.props:
                    if prop.visible(t):
                        canvas.draw(prop.item)
            else:
                # first frame is rendered without any updates
                canvas = Canvas()
                if limits:
                    canvas.limits = limits
                for prop in self.props:
                    if prop.visible(t):
                        canvas.draw(prop.item)
            file_path = directory + '/' + file_name + str(t) + '.png'
            canvas.save(file_path, overwrite=True, show=False)
