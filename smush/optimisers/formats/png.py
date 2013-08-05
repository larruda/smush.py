import os.path

from ..optimiser import Optimiser


class OptimisePNG(Optimiser):
    """
    Optimises pngs. Uses pngnq (http://pngnq.sourceforge.net/) to quantise them, then uses pngcrush
    (http://pmt.sourceforge.net/pngcrush/) to crush them.
    """

    def __init__(self, **kwargs):
        super(OptimisePNG, self).__init__(**kwargs)

        if kwargs.get('quiet'):
            pngcrush = 'pngcrush -rem alla -brute -reduce -q "__INPUT__" "__OUTPUT__"'
        else:
            pngcrush = 'pngcrush -rem alla -brute -reduce "__INPUT__" "__OUTPUT__"'

        # the command to execute this optimiser
        self.commands = ('pngnq -n 256 -e "{obj.output_suffix}" "__INPUT__"'.format(obj=self), pngcrush)

        # format as returned by 'identify'
        self.format = "PNG"

    def _get_output_file_name(self):
        return os.path.splitext(self.input)[0] + self.output_suffix
