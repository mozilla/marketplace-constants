COLLECTION_COLORS = {
    'ruby': '#D46952',  # Red.
    'amber': '#ED8040',  # Orange.
    'topaz': '#FAD73B',  # Yellow.
    'emerald': '#8BC873',  # Green.
    'aquamarine': '#00C9A8',  # Blue.
    'sapphire': '#3A5990',  # Dark blue.
    'amethyst': '#8D4B87',  # Purple.
    'garnet': '#E77286',  # Magenta.
}

COLLECTION_COLORS_REVERSE = dict((v, k) for k, v in COLLECTION_COLORS.iteritems())

COLLECTION_COLORS_CHOICES = COLLECTION_COLORS_REVERSE.items()
