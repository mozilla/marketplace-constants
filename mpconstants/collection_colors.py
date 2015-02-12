COLLECTION_COLORS = {
    'sapphire': '#2d457e',  # Dark blue.
    'aquamarine': '#197b99',  # Blue.
    'emerald': '#1b8215',  # Green.
    'gold': '#ffb300', # Yellow.
    'amber': '#cc440d',  # Orange.
    'ruby': '#c93333',  # Red.
    'garnet': '#cc3388',  # Magenta.
    'amethyst': '#7a3675',  # Purple.
}

COLLECTION_COLORS_REVERSE = dict((v, k) for k, v in COLLECTION_COLORS.iteritems())

COLLECTION_COLORS_CHOICES = COLLECTION_COLORS_REVERSE.items()
