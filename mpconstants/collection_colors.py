COLLECTION_COLORS = {
    'ruby': '#CE001C',
    'amber': '#F78813',
    'emerald': '#00953F',
    'topaz': '#0099D0',
    'sapphire': '#1E1E9C',
    'amethyst': '#5A197E',
    'garnet': '#A20D55',
}

COLLECTION_COLORS_REVERSE = dict((v, k) for k, v in COLLECTION_COLORS.iteritems())

COLLECTION_COLORS_CHOICES = COLLECTION_COLORS_REVERSE.items()
