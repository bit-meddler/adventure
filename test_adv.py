import adv_abs as ADV

rooms = {
    "Front Garden" : {
        "navigation" : ["Living Room"],
        "desc_short" : "The Front Garden",
        "desc_long"  : "It is overgrown, with a large thorny bush",
    },
    "Living Room" : {
        "navigation" : ["Cellar Landing", None, "Front Garden"],
        "desc_short" : "The Living Room",
        "desc_long"  : "It is full of ramshackle furniture",
    },
    "Cellar Landing": {
        "navigation" : ["Dining Room", None, "Living Room"],
        "desc_short" : "The Cellar Landing",
        "desc_long"  : "The carpet is lose",
    },
    "Dining Room": {
        "navigation" : ["Kitchen", None, "Cellar Landing", "Stairs"],
        "desc_short" : "The Dining Room",
        "desc_long"  : "CLuttered with DVDs and many books",
    },
    "Kitchen": {
        "navigation" : [None, None, "Dining Room", "Back Yard"],
        "desc_short" : "The KItchen",
        "desc_long"  : "It needs a paint job",
    },
    "Back Yard": {
        "navigation" : [None, "Kitchen"],
        "desc_short" : "The Back Yard",
        "desc_long"  : "Various plant pots are scattered around",
    },
    "Stairs": {
        "navigation" : [None,None,None,None"Upstairs Landing", "Dining Room"],
        "desc_short" : "The Stairs",
        "desc_long"  : "There's nothing unusual about them",
    },
"""    "": {
        "navigation" : [""],
        "desc_short" : "",
        "desc_long"  : "",
    },
    "": {
        "navigation" : [""],
        "desc_short" : "",
        "desc_long"  : "",
    },
    "": {
        "navigation" : [""],
        "desc_short" : "",
        "desc_long"  : "",
    },
    "": {
        "navigation" : [""],
        "desc_short" : "",
        "desc_long"  : "",
    }, """
}
items = {
    "Door Mat" : {
        "name" : "Door Mat",
        "syns" : "Welcome Mat,Mat",
        "visi" : True,
        "desc_short" : "Door Mat"
        "desc_long"  : "It say's 'Welcome'",
        "actions"    : ["get"]
    },
    "Front Door Key" : {
        "name" : "Front Door Key",
        "syns" : "Key",
        "visi" : False,
        "desc_short" : "Front Door Key"
        "desc_long"  : "It's on a fob that says 'Timpson'",
        "actions"    : ["get","use"]
    },
"""        "" : {
        "name" : "",
        "syns" : "",
        "visi" : True,
        "desc_short" : ""
        "desc_long"  : "",
        "actions"    : "",
    }, """
}