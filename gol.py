import urwid
from model import GameofLife

UPDATE_INTERVAL = 0.2

PALETTE = [
    ('red', 'dark red', ''),
    ('green', 'dark green', ''),
    ('selected', '', 'yellow'),
    ('black','black',''),
    ('blue','dark blue',''),
    ('greenl', 'light green', ''),
    ('yellow', 'yellow', '')
]

STATES = {
    1 : "Initialize - press s for Spaceship, g for Glider , r for Random",
    2 : "Pause Game - press p to Pause Game ",
    3 : "Resume Game - press r to Resume or i to ReInitialize Grid"
}

#
# Game controller
# Manages keyboard input to Initialize, start, pause and stop game and renders view
#
class GameController(object):
    def __init__(self):
        self._header = urwid.Text( [('red',u"Conways Game of Life"), ('green',u" Christmas Edition")])
        self._status = urwid.Text( ('red',u""))
        cols, rows = urwid.raw_display.Screen().get_cols_rows()
        self.x = cols 
        self.y = rows - 5
        self._gridbox = urwid.Text('')
        self.game  = GameofLife(self.x, self.y, None)
        self.initialize()
        self.animate_alarm = None
        self.set_footer()
        
        self.main_layout = urwid.Pile([
            self._header,
            urwid.Divider(),
            self._gridbox,
            urwid.Divider(),
            self._status
        ])

    def initialize(self):
        self.state = 1
        self._gridbox.set_text(('black',['. ']* self.game.x * self.game.y))

    def set_footer(self):
        if self.state == 1:
            self._status.set_text(('red',self.game.get_initialize_text()))
        else:
            self._status.set_text(('red',STATES[self.state]))

    def on_start(self):
        self.state = 2
        self.animate()

    def on_pause(self):
        self.state = 3
        if self.animate_alarm:
            self.loop.remove_alarm(self.animate)
        self.animate_alarm = None

    def handle_input(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        else:
            self.manage_state(key)

        self.set_footer()

    def is_running(self):
        return self.state == 2

    def is_paused(self):
        return self.state == 3

    def is_initialized(self):
        return self.state == 1
    
    def manage_state(self, key):
        if self.is_initialized():
          """ Initialize Game """
          if key in self.game.get_initialize_keys(): self.game  = GameofLife(self.x, self.y, key)
          else: self.game  = GameofLife(self.x, self.y, 'r')
          self.on_start()
        if self.is_running() and key in ('p'):
          """ Pause Game """
          self.on_pause()
        if self.is_paused() and key in ('r'):
          """ Resume Game """
          self.on_start()
        if self.is_paused() and key in ('i'):
          """ Reset Game """
          self.initialize()

    def update_view(self):
        self.game.update()
        self._gridbox.set_text(self.game.get_data())
    
    # Program ticker
    def animate(self, loop=None, user_data=None):
        """update the graph and schedule the next update"""
        if self.state == 2:
          self.update_view()
          self.animate_alarm = self.loop.set_alarm_in(
               UPDATE_INTERVAL, self.animate)
    
    def run(self):
        self.loop = urwid.MainLoop(
            urwid.Filler(app.main_layout, valign='top'),
            PALETTE,
            unhandled_input=app.handle_input
        )
    
        self.loop.run() 
        
if __name__ == "__main__":
    app = GameController()
    app.run()
