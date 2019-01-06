# prototypes for an adventure system

class AdventureGame( object ):
    def __init__(self):
        self.locations = {}
        self.loc_count = -1
        self.loc_lut   = {}
        self.items     = {}
        self.itm_count = 0
        self.itm_lut   = {}
        self.player = Player( self )
        # Room 0 is for deleted or destroyed items
        _ = self.createRoom( "The Void" )

    def createRoom( self, name ):
        new_room = Room( name, self )
        self.locations[ name ] = new_room
        self.loc_count += 1
        new_room.ID = self.loc_count
        self.loc_lut[ new_room.ID ] = name
        return new_room

    def createItem( self, name ):
        new_item = Item( name, self )
        self.items[ name ] = new_item
        self.itm_count += 1
        new_item.ID = self.itm_count
        self.itm_lut[ new_room.ID ] = name
        return new_item

    def play( self ):
        self.playing = True
        while( self.playing ):
            # prepare language
            # get location
            curr_loc_id = self.player.location
            curr_loc_name = self.loc_lut[ curr_loc_id ]
            curr_loc = self.locations[ curr_loc_name ]
            # get default actions
            # get nouns (items in location)
            loc_items = curr_loc.getContents()
            # get verbs enabled by nouns
            # register synonyms

            # describe situation
            # room
            print( "You are {} {}.".format( curr_loc.retort() ) )
            # contents
            print( curr_loc.listContents( loc_items ) )
            # exits
            print( curr_loc.getExits() )

            # get command

            # parse to verb [prep] noun [[artical] [prep2] [noun2]]
            verb = "move"
            noun = "north"

            # attempt to execute action


class Aobj( object ):
    def __init__( self, name, game ):
        self.name = name
        self.game = game
        self.noun = ""
        self.verb = ""
        self.ID   = -1
        self.visible = True
        # descriptions
        self.desc_short = ""
        self.desc_long  = ""


class Item( Aobj ):
    """ Item """
    def __init__( self, name, game ):
        super( Item, self ).__init__( name, game )
        self.location = -1
        self.actions = {}
        self.complaints = {}

    def moveTo( self, target ):
        new_loc  = self.game.locations[ target ]
        old_name = self.game.loc_lut[ self.location ]
        old_loc  = self.game.locations[ old_name ]
        old_loc.contents.remove( self )
        new_loc.contents.append( self )
        self.location = new_loc.ID

    def doAction( self, verb, other=None ):
        pass


class Room( Aobj ):
    """ Room """
    NAVIGATION_DIRECTIONS = ( "north", "east", "south", "west", "up", "down" )
    def __init__( self, name, game ):
        super( Room, self ).__init__( name, game )
        self.navigation  = [ None for x in self.NAVIGATION_DIRECTIONS ]
        self.contents    = []
        self.population  = []
        self.encountered = False
        self.preposition = ""

    def retort( self ):
        if( self.encountered ):
            return self.preposition, self.desc_short
        else:
            self.encountered = True
            return self.preposition, self.desc_short + ".  " + self.desc_long

    def getExits( self ):
        info = ""
        exits = []
        for i, orient in enumerate( self.NAVIGATION_DIRECTIONS ):
            if( not self.navigation[ i ] is None ):
                exits.append( orient )
        num_exits = len( exits )
        if( num_exits > 1 ):
            info = "There are exits to the {} and {}.".format( ",".join( exits[:-1] ), exits[-1] )
        elif( num_exits > 0 ):
            info = "There is an exit to the {}.".format( exits[0] )
        else:   
            info = "No exits are visible."
        return info

    def getContents( self ):
        items = []
        for item in self.contents:
            if( item.visible ):
                items.append( item.desc_short )
        for npc in self.population:
            if( npc.visible ):
                items.append( npc.desc_short )
        return items

    def listContents( self, items=None ):
        if( items is None ):
            items = self.getContents
        info = ""
        num_items = len( items )
        if( num_items > 1 ):
            info = "There are {} and {}.".format( ",".join( items[:-1] ), items[-1] )
        elif( num_items > 0 ):
            info = "There is {}.".format( items[0] )
        else:   
            info = "Nothing special is visible."
        return info

    def nav( self, orient ):
        idx = self.NAVIGATION_DIRECTIONS.index( orient )
        return self.navigation[ idx ]


class Actor( Aobj ):
    """ Actor """
    def __init__( self, name, game ):
        super( Actor, self ).__init__( name, game )


class Player( Actor ):
    """ Player """
    def __init__( self, game ):
        super( Player, self ).__init__( "Player", game )
        self.location = -1
        self.ID = -1
        self.contents = [] # inventory
        self.actions = {}