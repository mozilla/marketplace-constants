FEED_COLORS = {
    'ruby': '#CE001C',
    'amber': '#F78813',
    'emerald': '#00953F',
    'topaz': '#0099D0',
    'sapphire': '#1E1E9C',
    'amethyst': '#5A197E',
    'garnet': '#A20D55',
}

FEED_COLORS_REVERSE = dict((v, k) for k, v in FEED_COLORS.iteritems())

FEED_COLOR_CHOICES = FEED_COLORS_REVERSE.items()
