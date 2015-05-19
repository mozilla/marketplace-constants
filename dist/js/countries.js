(function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define([], factory);
    } else if (typeof exports === 'object') {
        // Node. Does not work with strict CommonJS, but
        // only CommonJS-like environments that support module.exports,
        // like Node.
        module.exports = factory();
    } else {
        // Browser globals (root is window).
        root.returnExports = factory();
    }
}(this, function() {
    return {"COUNTRY_DETAILS": {"AGO": {"name": "Angola", "adolescent": false, "weight": 0, "id": 64, "ratingsbody": null, "slug": "ao", "special": false}, "DZA": {"name": "Algeria", "adolescent": false, "weight": 0, "id": 61, "ratingsbody": null, "slug": "dz", "special": false}, "BGD": {"weight": 0, "name": "Bangladesh", "adolescent": true, "ratingsbody": null, "mcc": 470, "id": 31, "special": false, "slug": "bd"}, "QAT": {"name": "Qatar", "adolescent": false, "weight": 0, "id": 195, "ratingsbody": null, "slug": "qa", "special": false}, "BGR": {"name": "Bulgaria", "adolescent": false, "weight": 0, "id": 88, "ratingsbody": null, "slug": "bg", "special": false}, "PAK": {"name": "Pakistan", "adolescent": false, "weight": 0, "id": 187, "ratingsbody": null, "slug": "pk", "special": false}, "CPV": {"name": "Cabo Verde", "adolescent": false, "weight": 0, "id": 93, "ratingsbody": null, "slug": "cv", "special": false}, "VNM": {"name": "Viet Nam", "adolescent": false, "weight": 0, "id": 244, "ratingsbody": null, "slug": "vn", "special": false}, "PSE": {"name": "Palestine, State of", "adolescent": false, "weight": 0, "id": 189, "ratingsbody": null, "slug": "ps", "special": false}, "TZA": {"name": "Tanzania", "adolescent": true, "mcc": 640, "weight": 0, "id": 44, "slug": "tz", "special": false}, "BWA": {"name": "Botswana", "adolescent": true, "mcc": 652, "weight": 0, "id": 45, "slug": "bw", "special": false}, "SPM": {"name": "Saint Pierre and Miquelon", "adolescent": false, "weight": 0, "id": 204, "ratingsbody": null, "slug": "pm", "special": false}, "KNA": {"name": "Saint Kitts and Nevis", "adolescent": false, "weight": 0, "id": 201, "ratingsbody": null, "slug": "kn", "special": false}, "MMR": {"name": "Myanmar", "adolescent": true, "mcc": 414, "weight": 0, "id": 53, "slug": "mm", "special": false}, "GIB": {"name": "Gibraltar", "adolescent": false, "weight": 0, "id": 125, "ratingsbody": null, "slug": "gi", "special": false}, "DJI": {"name": "Djibouti", "adolescent": false, "weight": 0, "id": 107, "ratingsbody": null, "slug": "dj", "special": false}, "GIN": {"name": "Guinea-Conakry", "adolescent": true, "mcc": 611, "weight": 0, "id": 55, "slug": "gn", "special": false}, "FIN": {"name": "Finland", "adolescent": false, "weight": 0, "id": 117, "ratingsbody": null, "slug": "fi", "special": false}, "THA": {"name": "Thailand", "adolescent": false, "weight": 0, "id": 229, "ratingsbody": null, "slug": "th", "special": false}, "SYC": {"name": "Seychelles", "adolescent": false, "weight": 0, "id": 210, "ratingsbody": null, "slug": "sc", "special": false}, "NPL": {"name": "Nepal", "adolescent": false, "weight": 0, "id": 177, "ratingsbody": null, "slug": "np", "special": false}, "LAO": {"name": "Lao People\'s Democratic Republic", "adolescent": false, "weight": 0, "id": 150, "ratingsbody": null, "slug": "la", "special": false}, "YEM": {"name": "Yemen", "adolescent": false, "weight": 0, "id": 249, "ratingsbody": null, "slug": "ye", "special": false}, "PHL": {"name": "Philippines", "adolescent": true, "ratingsbody": null, "low_memory": true, "mcc": 515, "id": 35, "weight": 0, "slug": "ph"}, "ZAF": {"weight": 0, "name": "South Africa", "adolescent": false, "ratingsbody": null, "mcc": 655, "id": 37, "special": false, "slug": "za"}, "KIR": {"name": "Kiribati", "adolescent": false, "weight": 0, "id": 146, "ratingsbody": null, "slug": "ki", "special": false}, "ROU": {"name": "Romania", "adolescent": false, "weight": 0, "id": 197, "ratingsbody": null, "slug": "ro", "special": false}, "SYR": {"name": "Syrian Arab Republic", "adolescent": false, "weight": 0, "id": 227, "ratingsbody": null, "slug": "sy", "special": false}, "MAC": {"name": "Macao", "adolescent": false, "weight": 0, "id": 158, "ratingsbody": null, "slug": "mo", "special": false}, "MAF": {"weight": 0, "name": "Saint Martin (French part)", "adolescent": false, "ratingsbody": null, "mcc": 340, "id": 255, "special": false, "slug": "mf"}, "NIU": {"name": "Niue", "adolescent": false, "weight": 0, "id": 182, "ratingsbody": null, "slug": "nu", "special": false}, "DMA": {"name": "Dominica", "adolescent": false, "weight": 0, "id": 108, "ratingsbody": null, "slug": "dm", "special": false}, "BEN": {"name": "Benin", "adolescent": false, "weight": 0, "id": 79, "ratingsbody": null, "slug": "bj", "special": false}, "GUF": {"name": "French Guiana", "adolescent": false, "weight": 0, "id": 118, "ratingsbody": null, "slug": "gf", "special": false}, "BEL": {"name": "Belgium", "adolescent": false, "weight": 0, "id": 77, "ratingsbody": null, "slug": "be", "special": false}, "GUM": {"name": "Guam", "adolescent": false, "weight": 0, "id": 129, "ratingsbody": null, "slug": "gu", "special": false}, "GBR": {"weight": 0, "name": "United Kingdom", "adolescent": true, "ratingsbody": "PEGI", "mcc": 235, "id": 4, "special": false, "slug": "uk"}, "BES": {"name": "Bonaire, Sint Eustatius and Saba", "adolescent": false, "weight": 0, "id": 252, "ratingsbody": null, "slug": "bq", "special": false}, "GUY": {"name": "Guyana", "adolescent": false, "weight": 0, "id": 131, "ratingsbody": null, "slug": "gy", "special": false}, "CRI": {"weight": 0, "name": "Costa Rica", "adolescent": true, "ratingsbody": "ESRB", "mcc": 712, "id": 27, "special": false, "slug": "cr"}, "CMR": {"name": "Cameroon", "adolescent": true, "mcc": 624, "weight": 0, "id": 42, "slug": "cm", "special": false}, "LSO": {"name": "Lesotho", "adolescent": false, "weight": 0, "id": 153, "ratingsbody": null, "slug": "ls", "special": false}, "HUN": {"weight": 0, "name": "Hungary", "adolescent": true, "ratingsbody": "PEGI", "mcc": 216, "id": 13, "special": false, "slug": "hu"}, "TTO": {"name": "Trinidad and Tobago", "adolescent": false, "weight": 0, "id": 234, "ratingsbody": null, "slug": "tt", "special": false}, "PAN": {"weight": 0, "name": "Panama", "adolescent": true, "ratingsbody": "ESRB", "mcc": 714, "id": 28, "special": false, "slug": "pa"}, "TCD": {"name": "Chad", "adolescent": false, "weight": 0, "id": 95, "ratingsbody": null, "slug": "td", "special": false}, "GEO": {"name": "Georgia", "adolescent": false, "weight": 0, "id": 123, "ratingsbody": null, "slug": "ge", "special": false}, "SXM": {"name": "Sint Maarten (Dutch part)", "adolescent": false, "weight": 0, "id": 256, "ratingsbody": null, "slug": "sx", "special": false}, "TCA": {"name": "Turks and Caicos Islands", "adolescent": false, "weight": 0, "id": 237, "ratingsbody": null, "slug": "tc", "special": false}, "MHL": {"name": "Marshall Islands", "adolescent": false, "weight": 0, "id": 164, "ratingsbody": null, "slug": "mh", "special": false}, "BLZ": {"name": "Belize", "adolescent": false, "weight": 0, "id": 78, "ratingsbody": null, "slug": "bz", "special": false}, "NFK": {"name": "Norfolk Island", "adolescent": false, "weight": 0, "id": 183, "ratingsbody": null, "slug": "nf", "special": false}, "VGB": {"name": "Virgin Islands, British", "adolescent": false, "weight": 0, "id": 245, "ratingsbody": null, "slug": "vg", "special": false}, "BLR": {"name": "Belarus", "adolescent": false, "weight": 0, "id": 76, "ratingsbody": null, "slug": "by", "special": false}, "BLM": {"name": "Saint Barth\u00e9lemy", "adolescent": false, "weight": 0, "id": 253, "ratingsbody": null, "slug": "bl", "special": false}, "GRD": {"name": "Grenada", "adolescent": false, "weight": 0, "id": 127, "ratingsbody": null, "slug": "gd", "special": false}, "GRC": {"weight": 0, "name": "Greece", "adolescent": true, "ratingsbody": "PEGI", "mcc": 202, "id": 17, "special": false, "slug": "gr"}, "VAT": {"name": "Holy See", "adolescent": false, "weight": 0, "id": 134, "ratingsbody": null, "slug": "va", "special": false}, "GRL": {"name": "Greenland", "adolescent": false, "weight": 0, "id": 126, "ratingsbody": null, "slug": "gl", "special": false}, "AND": {"name": "Andorra", "adolescent": false, "weight": 0, "id": 63, "ratingsbody": null, "slug": "ad", "special": false}, "MOZ": {"name": "Mozambique", "adolescent": false, "weight": 0, "id": 174, "ratingsbody": null, "slug": "mz", "special": false}, "TJK": {"name": "Tajikistan", "adolescent": false, "weight": 0, "id": 228, "ratingsbody": null, "slug": "tj", "special": false}, "MEX": {"weight": 0, "name": "Mexico", "adolescent": false, "ratingsbody": "ESRB", "mcc": 334, "id": 12, "special": false, "slug": "mx"}, "LCA": {"name": "Saint Lucia", "adolescent": false, "weight": 0, "id": 202, "ratingsbody": null, "slug": "lc", "special": false}, "IND": {"name": "India", "adolescent": true, "ratingsbody": null, "low_memory": true, "mcc": 405, "id": 32, "weight": 0, "slug": "in"}, "NOR": {"name": "Norway", "adolescent": false, "weight": 0, "id": 185, "ratingsbody": null, "slug": "no", "special": false}, "FJI": {"name": "Fiji", "adolescent": false, "weight": 0, "id": 116, "ratingsbody": null, "slug": "fj", "special": false}, "HND": {"name": "Honduras", "adolescent": false, "weight": 0, "id": 135, "ratingsbody": null, "slug": "hn", "special": false}, "DOM": {"name": "Dominican Republic", "adolescent": false, "weight": 0, "id": 109, "ratingsbody": null, "slug": "do", "special": false}, "FSM": {"name": "Micronesia, Federated States of", "adolescent": false, "weight": 0, "id": 168, "ratingsbody": null, "slug": "fm", "special": false}, "PER": {"weight": 0, "name": "Peru", "adolescent": false, "ratingsbody": "ESRB", "mcc": 716, "id": 18, "special": false, "slug": "pe"}, "REU": {"name": "R\u00e9union", "adolescent": false, "weight": 0, "id": 196, "ratingsbody": null, "slug": "re", "special": false}, "VUT": {"name": "Vanuatu", "adolescent": true, "mcc": 541, "weight": 0, "id": 47, "slug": "vu", "special": false}, "GNQ": {"name": "Equatorial Guinea", "adolescent": false, "weight": 0, "id": 110, "ratingsbody": null, "slug": "gq", "special": false}, "COD": {"name": "Congo, Democratic Republic of the", "adolescent": false, "weight": 0, "id": 100, "ratingsbody": null, "slug": "cd", "special": false}, "COG": {"name": "Congo", "adolescent": false, "weight": 0, "id": 99, "ratingsbody": null, "slug": "cg", "special": false}, "GLP": {"name": "Guadeloupe", "adolescent": false, "weight": 0, "id": 128, "ratingsbody": null, "slug": "gp", "special": false}, "COK": {"name": "Cook Islands", "adolescent": false, "weight": 0, "id": 101, "ratingsbody": null, "slug": "ck", "special": false}, "COM": {"name": "Comoros", "adolescent": false, "weight": 0, "id": 98, "ratingsbody": null, "slug": "km", "special": false}, "COL": {"weight": 0, "name": "Colombia", "adolescent": false, "ratingsbody": "ESRB", "mcc": 732, "id": 9, "special": false, "slug": "co"}, "MDA": {"name": "Moldova, Republic of", "adolescent": false, "weight": 0, "id": 169, "ratingsbody": null, "slug": "md", "special": false}, "GGY": {"name": "Guernsey", "adolescent": false, "weight": 0, "id": 130, "ratingsbody": null, "slug": "gg", "special": false}, "MDG": {"name": "Madagascar", "adolescent": true, "mcc": 646, "weight": 0, "id": 49, "slug": "mg", "special": false}, "MDV": {"name": "Maldives", "adolescent": false, "weight": 0, "id": 162, "ratingsbody": null, "slug": "mv", "special": false}, "SRB": {"weight": 0, "name": "Serbia", "adolescent": true, "ratingsbody": "PEGI", "mcc": 220, "id": 16, "special": false, "slug": "rs"}, "LTU": {"name": "Lithuania", "adolescent": true, "mcc": 370, "weight": 0, "id": 38, "slug": "lt", "special": false}, "RWA": {"name": "Rwanda", "adolescent": false, "weight": 0, "id": 198, "ratingsbody": null, "slug": "rw", "special": false}, "ZMB": {"name": "Zambia", "adolescent": false, "weight": 0, "id": 250, "ratingsbody": null, "slug": "zm", "special": false}, "TWN": {"name": "Taiwan", "adolescent": true, "mcc": 466, "weight": 0, "id": 57, "slug": "tw", "special": false}, "WLF": {"name": "Wallis and Futuna", "adolescent": false, "weight": 0, "id": 247, "ratingsbody": null, "slug": "wf", "special": false}, "JEY": {"name": "Jersey", "adolescent": false, "weight": 0, "id": 144, "ratingsbody": null, "slug": "je", "special": false}, "AZE": {"name": "Azerbaijan", "adolescent": false, "weight": 0, "id": 72, "ratingsbody": null, "slug": "az", "special": false}, "AUS": {"name": "Australia", "adolescent": false, "weight": 0, "id": 70, "ratingsbody": null, "slug": "au", "special": false}, "AUT": {"name": "Austria", "adolescent": false, "weight": 0, "id": 71, "ratingsbody": null, "slug": "at", "special": false}, "VEN": {"weight": 0, "name": "Venezuela", "adolescent": false, "ratingsbody": "ESRB", "mcc": 734, "id": 10, "special": false, "slug": "ve"}, "PLW": {"name": "Palau", "adolescent": false, "weight": 0, "id": 188, "ratingsbody": null, "slug": "pw", "special": false}, "ALB": {"name": "Albania", "adolescent": false, "weight": 0, "id": 60, "ratingsbody": null, "slug": "al", "special": false}, "ALA": {"name": "\u00c5land Islands", "adolescent": false, "weight": 0, "id": 59, "ratingsbody": null, "slug": "ax", "special": false}, "RUS": {"name": "Russia", "adolescent": true, "mcc": 250, "weight": 0, "id": 36, "slug": "ru", "special": false}, "MKD": {"name": "Macedonia, the former Yugoslav Republic of", "adolescent": false, "weight": 0, "id": 159, "ratingsbody": null, "slug": "mk", "special": false}, "WSM": {"name": "Samoa", "adolescent": false, "weight": 0, "id": 206, "ratingsbody": null, "slug": "ws", "special": false}, "UKR": {"name": "Ukraine", "adolescent": false, "weight": 0, "id": 240, "ratingsbody": null, "slug": "ua", "special": false}, "GNB": {"name": "Guinea-Bissau", "adolescent": true, "mcc": 632, "weight": 0, "id": 46, "slug": "gw", "special": false}, "TON": {"name": "Tonga", "adolescent": false, "weight": 0, "id": 233, "ratingsbody": null, "slug": "to", "special": false}, "CAN": {"name": "Canada", "adolescent": false, "weight": 0, "id": 92, "ratingsbody": null, "slug": "ca", "special": false}, "KOR": {"name": "Korea, Republic of", "adolescent": false, "weight": 0, "id": 147, "ratingsbody": null, "slug": "kr", "special": false}, "AIA": {"name": "Anguilla", "adolescent": false, "weight": 0, "id": 65, "ratingsbody": null, "slug": "ai", "special": false}, "CAF": {"name": "Central African Republic", "adolescent": true, "mcc": 623, "weight": 0, "id": 54, "slug": "cf", "special": false}, "SVK": {"name": "Slovakia", "adolescent": false, "weight": 0, "id": 214, "ratingsbody": null, "slug": "sk", "special": false}, "SOM": {"name": "Somalia", "adolescent": false, "weight": 0, "id": 217, "ratingsbody": null, "slug": "so", "special": false}, "ERI": {"name": "Eritrea", "adolescent": false, "weight": 0, "id": 111, "ratingsbody": null, "slug": "er", "special": false}, "GAB": {"name": "Gabon", "adolescent": false, "weight": 0, "id": 121, "ratingsbody": null, "slug": "ga", "special": false}, "IRQ": {"name": "Iraq", "adolescent": false, "weight": 0, "id": 139, "ratingsbody": null, "slug": "iq", "special": false}, "MTQ": {"name": "Martinique", "adolescent": false, "weight": 0, "id": 165, "ratingsbody": null, "slug": "mq", "special": false}, "IRL": {"name": "Ireland", "adolescent": false, "weight": 0, "id": 140, "ratingsbody": null, "slug": "ie", "special": false}, "ABW": {"name": "Aruba", "adolescent": false, "weight": 0, "id": 69, "ratingsbody": null, "slug": "aw", "special": false}, "NZL": {"name": "New Zealand", "adolescent": false, "weight": 0, "id": 180, "ratingsbody": null, "slug": "nz", "special": false}, "JAM": {"name": "Jamaica", "adolescent": false, "weight": 0, "id": 143, "ratingsbody": null, "slug": "jm", "special": false}, "NCL": {"name": "New Caledonia", "adolescent": false, "weight": 0, "id": 179, "ratingsbody": null, "slug": "nc", "special": false}, "ARE": {"name": "United Arab Emirates", "adolescent": false, "weight": 0, "id": 241, "ratingsbody": null, "slug": "ae", "special": false}, "ARG": {"weight": 0, "name": "Argentina", "adolescent": true, "ratingsbody": "ESRB", "mcc": 722, "id": 20, "special": false, "slug": "ar"}, "BHS": {"name": "Bahamas", "adolescent": false, "weight": 0, "id": 73, "ratingsbody": null, "slug": "bs", "special": false}, "BHR": {"name": "Bahrain", "adolescent": false, "weight": 0, "id": 74, "ratingsbody": null, "slug": "bh", "special": false}, "ARM": {"name": "Armenia", "adolescent": false, "weight": 0, "id": 68, "ratingsbody": null, "slug": "am", "special": false}, "PNG": {"name": "Papua New Guinea", "adolescent": false, "weight": 0, "id": 190, "ratingsbody": null, "slug": "pg", "special": false}, "LIE": {"name": "Liechtenstein", "adolescent": false, "weight": 0, "id": 156, "ratingsbody": null, "slug": "li", "special": false}, "EGY": {"name": "Egypt", "adolescent": true, "mcc": 602, "weight": 0, "id": 43, "slug": "eg", "special": false}, "NAM": {"name": "Namibia", "adolescent": false, "weight": 0, "id": 175, "ratingsbody": null, "slug": "na", "special": false}, "BOL": {"name": "Bolivia, Plurinational State of", "adolescent": false, "weight": 0, "id": 82, "ratingsbody": null, "slug": "bo", "special": false}, "GHA": {"name": "Ghana", "adolescent": false, "weight": 0, "id": 124, "ratingsbody": null, "slug": "gh", "special": false}, "CCK": {"name": "Cocos (Keeling) Islands", "adolescent": false, "weight": 0, "id": 97, "ratingsbody": null, "slug": "cc", "special": false}, "JOR": {"name": "Jordan", "adolescent": true, "mcc": 416, "weight": 0, "id": 51, "slug": "jo", "special": false}, "LBR": {"name": "Liberia", "adolescent": false, "weight": 0, "id": 154, "ratingsbody": null, "slug": "lr", "special": false}, "LBY": {"name": "Libya", "adolescent": false, "weight": 0, "id": 155, "ratingsbody": null, "slug": "ly", "special": false}, "MYS": {"name": "Malaysia", "adolescent": false, "weight": 0, "id": 161, "ratingsbody": null, "slug": "my", "special": false}, "IOT": {"name": "British Indian Ocean Territory", "adolescent": false, "weight": 0, "id": 86, "ratingsbody": null, "slug": "io", "special": false}, "PRI": {"name": "Puerto Rico", "adolescent": false, "weight": 0, "id": 194, "ratingsbody": null, "slug": "pr", "special": false}, "MYT": {"name": "Mayotte", "adolescent": false, "weight": 0, "id": 167, "ratingsbody": null, "slug": "yt", "special": false}, "PRT": {"name": "Portugal", "adolescent": false, "weight": 0, "id": 193, "ratingsbody": null, "slug": "pt", "special": false}, "KHM": {"name": "Cambodia", "adolescent": false, "weight": 0, "id": 91, "ratingsbody": null, "slug": "kh", "special": false}, "PRY": {"name": "Paraguay", "adolescent": false, "weight": 0, "id": 191, "ratingsbody": null, "slug": "py", "special": false}, "HKG": {"name": "Hong Kong", "adolescent": false, "weight": 0, "id": 136, "ratingsbody": null, "slug": "hk", "special": false}, "SAU": {"name": "Saudi Arabia", "adolescent": false, "weight": 0, "id": 209, "ratingsbody": null, "slug": "sa", "special": false}, "LBN": {"name": "Lebanon", "adolescent": false, "weight": 0, "id": 152, "ratingsbody": null, "slug": "lb", "special": false}, "SVN": {"name": "Slovenia", "adolescent": false, "weight": 0, "id": 215, "ratingsbody": null, "slug": "si", "special": false}, "BFA": {"name": "Burkina Faso", "adolescent": false, "weight": 0, "id": 89, "ratingsbody": null, "slug": "bf", "special": false}, "CHE": {"name": "Switzerland", "adolescent": false, "weight": 0, "id": 226, "ratingsbody": null, "slug": "ch", "special": false}, "MRT": {"name": "Mauritania", "adolescent": false, "weight": 0, "id": 166, "ratingsbody": null, "slug": "mr", "special": false}, "HRV": {"name": "Croatia", "adolescent": false, "weight": 0, "id": 102, "ratingsbody": null, "slug": "hr", "special": false}, "CHL": {"weight": 0, "name": "Chile", "adolescent": true, "ratingsbody": "ESRB", "mcc": 730, "id": 23, "special": false, "slug": "cl"}, "CHN": {"weight": 0, "name": "China", "adolescent": true, "ratingsbody": null, "mcc": 460, "id": 21, "special": true, "slug": "cn"}, "SMR": {"name": "San Marino", "adolescent": false, "weight": 0, "id": 207, "ratingsbody": null, "slug": "sm", "special": false}, "MAR": {"name": "Morocco", "adolescent": false, "weight": 0, "id": 173, "ratingsbody": null, "slug": "ma", "special": false}, "URY": {"weight": 0, "name": "Uruguay", "adolescent": false, "ratingsbody": "ESRB", "mcc": 748, "id": 19, "special": false, "slug": "uy"}, "CXR": {"name": "Christmas Island", "adolescent": false, "weight": 0, "id": 96, "ratingsbody": null, "slug": "cx", "special": false}, "BVT": {"name": "Bouvet Island", "adolescent": false, "weight": 0, "id": 85, "ratingsbody": null, "slug": "bv", "special": false}, "VIR": {"name": "Virgin Islands, U.S.", "adolescent": false, "weight": 0, "id": 246, "ratingsbody": null, "slug": "vi", "special": false}, "NIC": {"weight": 0, "name": "Nicaragua", "adolescent": true, "ratingsbody": "ESRB", "mcc": 710, "id": 29, "special": false, "slug": "ni"}, "KAZ": {"name": "Kazakhstan", "adolescent": false, "weight": 0, "id": 145, "ratingsbody": null, "slug": "kz", "special": false}, "PYF": {"name": "French Polynesia", "adolescent": false, "weight": 0, "id": 119, "ratingsbody": null, "slug": "pf", "special": false}, "NGA": {"name": "Nigeria", "adolescent": false, "weight": 0, "id": 181, "ratingsbody": null, "slug": "ng", "special": false}, "DEU": {"weight": 0, "name": "Germany", "adolescent": true, "ratingsbody": "USK", "mcc": 262, "id": 14, "special": false, "slug": "de"}, "LKA": {"name": "Sri Lanka", "adolescent": false, "weight": 0, "id": 220, "ratingsbody": null, "slug": "lk", "special": false}, "FLK": {"name": "Falkland Islands (Malvinas)", "adolescent": false, "weight": 0, "id": 114, "ratingsbody": null, "slug": "fk", "special": false}, "MWI": {"name": "Malawi", "adolescent": false, "weight": 0, "id": 160, "ratingsbody": null, "slug": "mw", "special": false}, "ETH": {"name": "Ethiopia", "adolescent": false, "weight": 0, "id": 113, "ratingsbody": null, "slug": "et", "special": false}, "MNP": {"name": "Northern Mariana Islands", "adolescent": false, "weight": 0, "id": 184, "ratingsbody": null, "slug": "mp", "special": false}, "UMI": {"name": "United States Minor Outlying Islands", "adolescent": false, "weight": 0, "id": 257, "ratingsbody": null, "slug": "um", "special": false}, "TKL": {"name": "Tokelau", "adolescent": false, "weight": 0, "id": 232, "ratingsbody": null, "slug": "tk", "special": false}, "TKM": {"name": "Turkmenistan", "adolescent": false, "weight": 0, "id": 236, "ratingsbody": null, "slug": "tm", "special": false}, "NLD": {"name": "Netherlands", "adolescent": false, "weight": 0, "id": 178, "ratingsbody": null, "slug": "nl", "special": false}, "BMU": {"name": "Bermuda", "adolescent": false, "weight": 0, "id": 80, "ratingsbody": null, "slug": "bm", "special": false}, "HMD": {"name": "Heard Island and McDonald Islands", "adolescent": false, "weight": 0, "id": 133, "ratingsbody": null, "slug": "hm", "special": false}, "MNE": {"weight": 0, "name": "Montenegro", "adolescent": true, "ratingsbody": "PEGI", "mcc": 297, "id": 15, "special": false, "slug": "me"}, "MNG": {"name": "Mongolia", "adolescent": false, "weight": 0, "id": 171, "ratingsbody": null, "slug": "mn", "special": false}, "AFG": {"name": "Afghanistan", "adolescent": false, "weight": 0, "id": 58, "ratingsbody": null, "slug": "af", "special": false}, "BDI": {"name": "Burundi", "adolescent": false, "weight": 0, "id": 90, "ratingsbody": null, "slug": "bi", "special": false}, "SHN": {"name": "Saint Helena, Ascension and Tristan da Cunha", "adolescent": false, "weight": 0, "id": 200, "ratingsbody": null, "slug": "sh", "special": false}, "ZWE": {"name": "Zimbabwe", "adolescent": false, "weight": 0, "id": 251, "ratingsbody": null, "slug": "zw", "special": false}, "HTI": {"name": "Haiti", "adolescent": false, "weight": 0, "id": 132, "ratingsbody": null, "slug": "ht", "special": false}, "LVA": {"name": "Latvia", "adolescent": false, "weight": 0, "id": 151, "ratingsbody": null, "slug": "lv", "special": false}, "BTN": {"name": "Bhutan", "adolescent": false, "weight": 0, "id": 81, "ratingsbody": null, "slug": "bt", "special": false}, "CZE": {"name": "Czech Republic", "adolescent": true, "mcc": 230, "weight": 0, "id": 34, "slug": "cz", "special": false}, "ATF": {"name": "French Southern Territories", "adolescent": false, "weight": 0, "id": 120, "ratingsbody": null, "slug": "tf", "special": false}, "ATG": {"name": "Antigua and Barbuda", "adolescent": false, "weight": 0, "id": 67, "ratingsbody": null, "slug": "ag", "special": false}, "MUS": {"name": "Mauritius", "adolescent": true, "mcc": 617, "weight": 0, "id": 50, "slug": "mu", "special": false}, "ATA": {"name": "Antarctica", "adolescent": false, "weight": 0, "id": 66, "ratingsbody": null, "slug": "aq", "special": false}, "LUX": {"name": "Luxembourg", "adolescent": false, "weight": 0, "id": 157, "ratingsbody": null, "slug": "lu", "special": false}, "ISR": {"name": "Israel", "adolescent": false, "weight": 0, "id": 142, "ratingsbody": null, "slug": "il", "special": false}, "IDN": {"name": "Indonesia", "adolescent": false, "weight": 0, "id": 138, "ratingsbody": null, "slug": "id", "special": false}, "SUR": {"name": "Suriname", "adolescent": false, "weight": 0, "id": 222, "ratingsbody": null, "slug": "sr", "special": false}, "ISL": {"name": "Iceland", "adolescent": false, "weight": 0, "id": 137, "ratingsbody": null, "slug": "is", "special": false}, "NER": {"name": "Niger", "adolescent": true, "mcc": 614, "weight": 0, "id": 52, "slug": "ne", "special": false}, "STP": {"name": "Sao Tome and Principe", "adolescent": false, "weight": 0, "id": 208, "ratingsbody": null, "slug": "st", "special": false}, "ECU": {"weight": 0, "name": "Ecuador", "adolescent": true, "ratingsbody": "ESRB", "mcc": 740, "id": 26, "special": false, "slug": "ec"}, "SEN": {"name": "Senegal", "adolescent": true, "mcc": 608, "weight": 0, "id": 41, "slug": "sn", "special": false}, "ASM": {"name": "American Samoa", "adolescent": false, "weight": 0, "id": 62, "ratingsbody": null, "slug": "as", "special": false}, "CUW": {"name": "Cura\u00e7ao", "adolescent": false, "weight": 0, "id": 254, "ratingsbody": null, "slug": "cw", "special": false}, "FRA": {"weight": 0, "name": "France", "adolescent": true, "ratingsbody": "PEGI", "mcc": 208, "id": 30, "special": false, "slug": "fr"}, "GMB": {"name": "Gambia", "adolescent": false, "weight": 0, "id": 122, "ratingsbody": null, "slug": "gm", "special": false}, "SSD": {"name": "South Sudan", "adolescent": false, "weight": 0, "id": 219, "ratingsbody": null, "slug": "ss", "special": false}, "FRO": {"name": "Faroe Islands", "adolescent": false, "weight": 0, "id": 115, "ratingsbody": null, "slug": "fo", "special": false}, "GTM": {"weight": 0, "name": "Guatemala", "adolescent": true, "ratingsbody": "ESRB", "mcc": 704, "id": 25, "special": false, "slug": "gt"}, "DNK": {"name": "Denmark", "adolescent": false, "weight": 0, "id": 106, "ratingsbody": null, "slug": "dk", "special": false}, "IMN": {"name": "Isle of Man", "adolescent": false, "weight": 0, "id": 141, "ratingsbody": null, "slug": "im", "special": false}, "CUB": {"name": "Cuba", "adolescent": false, "weight": 0, "id": 103, "ratingsbody": null, "slug": "cu", "special": false}, "SJM": {"name": "Svalbard and Jan Mayen", "adolescent": false, "weight": 0, "id": 223, "ratingsbody": null, "slug": "sj", "special": false}, "KEN": {"name": "Kenya", "adolescent": true, "mcc": 639, "weight": 0, "id": 56, "slug": "ke", "special": false}, "TUR": {"name": "Turkey", "adolescent": false, "weight": 0, "id": 235, "ratingsbody": null, "slug": "tr", "special": false}, "OMN": {"name": "Oman", "adolescent": false, "weight": 0, "id": 186, "ratingsbody": null, "slug": "om", "special": false}, "TUV": {"name": "Tuvalu", "adolescent": false, "weight": 0, "id": 238, "ratingsbody": null, "slug": "tv", "special": false}, "ITA": {"weight": 0, "name": "Italy", "adolescent": true, "ratingsbody": "PEGI", "mcc": 222, "id": 22, "special": false, "slug": "it"}, "BRN": {"name": "Brunei Darussalam", "adolescent": false, "weight": 0, "id": 87, "ratingsbody": null, "slug": "bn", "special": false}, "TUN": {"name": "Tunisia", "adolescent": true, "mcc": 605, "weight": 0, "id": 39, "slug": "tn", "special": false}, "PCN": {"name": "Pitcairn", "adolescent": false, "weight": 0, "id": 192, "ratingsbody": null, "slug": "pn", "special": false}, "BRB": {"name": "Barbados", "adolescent": false, "weight": 0, "id": 75, "ratingsbody": null, "slug": "bb", "special": false}, "BRA": {"weight": 0, "name": "Brazil", "adolescent": false, "ratingsbody": "CLASSIND", "mcc": 724, "id": 7, "special": false, "slug": "br"}, "TLS": {"name": "Timor-Leste", "adolescent": false, "weight": 0, "id": 230, "ratingsbody": null, "slug": "tl", "special": false}, "USA": {"weight": 1, "name": "United States", "adolescent": true, "ratingsbody": "ESRB", "mcc": 310, "id": 2, "special": false, "slug": "us"}, "SWE": {"name": "Sweden", "adolescent": false, "weight": 0, "id": 225, "ratingsbody": null, "slug": "se", "special": false}, "MSR": {"name": "Montserrat", "adolescent": false, "weight": 0, "id": 172, "ratingsbody": null, "slug": "ms", "special": false}, "SWZ": {"name": "Swaziland", "adolescent": false, "weight": 0, "id": 224, "ratingsbody": null, "slug": "sz", "special": false}, "CIV": {"name": "C\u00f4te d\'Ivoire", "adolescent": true, "mcc": 612, "weight": 0, "id": 40, "slug": "ci", "special": false}, "CYP": {"name": "Cyprus", "adolescent": false, "weight": 0, "id": 105, "ratingsbody": null, "slug": "cy", "special": false}, "BIH": {"name": "Bosnia and Herzegovina", "adolescent": false, "weight": 0, "id": 84, "ratingsbody": null, "slug": "ba", "special": false}, "SGP": {"name": "Singapore", "adolescent": false, "weight": 0, "id": 212, "ratingsbody": null, "slug": "sg", "special": false}, "SGS": {"name": "South Georgia and the South Sandwich Islands", "adolescent": false, "weight": 0, "id": 218, "ratingsbody": null, "slug": "gs", "special": false}, "UZB": {"name": "Uzbekistan", "adolescent": false, "weight": 0, "id": 243, "ratingsbody": null, "slug": "uz", "special": false}, "POL": {"weight": 0, "name": "Poland", "adolescent": true, "ratingsbody": "PEGI", "mcc": 260, "id": 11, "special": false, "slug": "pl"}, "KWT": {"name": "Kuwait", "adolescent": false, "weight": 0, "id": 148, "ratingsbody": null, "slug": "kw", "special": false}, "TGO": {"name": "Togo", "adolescent": false, "weight": 0, "id": 231, "ratingsbody": null, "slug": "tg", "special": false}, "CYM": {"name": "Cayman Islands", "adolescent": false, "weight": 0, "id": 94, "ratingsbody": null, "slug": "ky", "special": false}, "EST": {"name": "Estonia", "adolescent": false, "weight": 0, "id": 112, "ratingsbody": null, "slug": "ee", "special": false}, "ESP": {"weight": 0, "name": "Spain", "adolescent": true, "ratingsbody": "PEGI", "mcc": 214, "id": 8, "special": false, "slug": "es"}, "SLV": {"weight": 0, "name": "El Salvador", "adolescent": true, "ratingsbody": "ESRB", "mcc": 706, "id": 24, "special": false, "slug": "sv"}, "MLI": {"name": "Mali", "adolescent": true, "mcc": 610, "weight": 0, "id": 48, "slug": "ml", "special": false}, "VCT": {"name": "Saint Vincent and the Grenadines", "adolescent": false, "weight": 0, "id": 205, "ratingsbody": null, "slug": "vc", "special": false}, "MLT": {"name": "Malta", "adolescent": false, "weight": 0, "id": 163, "ratingsbody": null, "slug": "mt", "special": false}, "SLE": {"name": "Sierra Leone", "adolescent": false, "weight": 0, "id": 211, "ratingsbody": null, "slug": "sl", "special": false}, "SDN": {"name": "Sudan", "adolescent": false, "weight": 0, "id": 221, "ratingsbody": null, "slug": "sd", "special": false}, "SLB": {"name": "Solomon Islands", "adolescent": false, "weight": 0, "id": 216, "ratingsbody": null, "slug": "sb", "special": false}, "ESH": {"name": "Western Sahara", "adolescent": false, "weight": 0, "id": 248, "ratingsbody": null, "slug": "eh", "special": false}, "MCO": {"name": "Monaco", "adolescent": false, "weight": 0, "id": 170, "ratingsbody": null, "slug": "mc", "special": false}, "JPN": {"name": "Japan", "adolescent": true, "mcc": 440, "weight": 0, "id": 33, "slug": "jp", "special": false}, "KGZ": {"name": "Kyrgyzstan", "adolescent": false, "weight": 0, "id": 149, "ratingsbody": null, "slug": "kg", "special": false}, "UGA": {"name": "Uganda", "adolescent": false, "weight": 0, "id": 239, "ratingsbody": null, "slug": "ug", "special": false}, "NRU": {"name": "Nauru", "adolescent": false, "weight": 0, "id": 176, "ratingsbody": null, "slug": "nr", "special": false}}, "COUNTRIES": ["ABW", "AFG", "AGO", "AIA", "ALA", "ALB", "AND", "ARE", "ARG", "ARM", "ASM", "ATA", "ATF", "ATG", "AUS", "AUT", "AZE", "BDI", "BEL", "BEN", "BES", "BFA", "BGD", "BGR", "BHR", "BHS", "BIH", "BLM", "BLR", "BLZ", "BMU", "BOL", "BRA", "BRB", "BRN", "BTN", "BVT", "BWA", "CAF", "CAN", "CCK", "CHE", "CHL", "CHN", "CIV", "CMR", "COD", "COG", "COK", "COL", "COM", "CPV", "CRI", "CUB", "CUW", "CXR", "CYM", "CYP", "CZE", "DEU", "DJI", "DMA", "DNK", "DOM", "DZA", "ECU", "EGY", "ERI", "ESH", "ESP", "EST", "ETH", "FIN", "FJI", "FLK", "FRA", "FRO", "FSM", "GAB", "GBR", "GEO", "GGY", "GHA", "GIB", "GIN", "GLP", "GMB", "GNB", "GNQ", "GRC", "GRD", "GRL", "GTM", "GUF", "GUM", "GUY", "HKG", "HMD", "HND", "HRV", "HTI", "HUN", "IDN", "IMN", "IND", "IOT", "IRL", "IRQ", "ISL", "ISR", "ITA", "JAM", "JEY", "JOR", "JPN", "KAZ", "KEN", "KGZ", "KHM", "KIR", "KNA", "KOR", "KWT", "LAO", "LBN", "LBR", "LBY", "LCA", "LIE", "LKA", "LSO", "LTU", "LUX", "LVA", "MAC", "MAF", "MAR", "MCO", "MDA", "MDG", "MDV", "MEX", "MHL", "MKD", "MLI", "MLT", "MMR", "MNE", "MNG", "MNP", "MOZ", "MRT", "MSR", "MTQ", "MUS", "MWI", "MYS", "MYT", "NAM", "NCL", "NER", "NFK", "NGA", "NIC", "NIU", "NLD", "NOR", "NPL", "NRU", "NZL", "OMN", "PAK", "PAN", "PCN", "PER", "PHL", "PLW", "PNG", "POL", "PRI", "PRT", "PRY", "PSE", "PYF", "QAT", "REU", "ROU", "RUS", "RWA", "SAU", "SDN", "SEN", "SGP", "SGS", "SHN", "SJM", "SLB", "SLE", "SLV", "SMR", "SOM", "SPM", "SRB", "SSD", "STP", "SUR", "SVK", "SVN", "SWE", "SWZ", "SXM", "SYC", "SYR", "TCA", "TCD", "TGO", "THA", "TJK", "TKL", "TKM", "TLS", "TON", "TTO", "TUN", "TUR", "TUV", "TWN", "TZA", "UGA", "UKR", "UMI", "URY", "USA", "UZB", "VAT", "VCT", "VEN", "VGB", "VIR", "VNM", "VUT", "WLF", "WSM", "YEM", "ZAF", "ZMB", "ZWE"]};
}));
