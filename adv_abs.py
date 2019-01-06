# prototypes for an adventure system

class AdventureGame( object ):
    def __init__(self):
        self.locations = {}
        self.loc_count = 0
        self.loc_lut   = {}
        self.items     = {}
        self.itm_count = 0
        self.itm_lut   = {}

    def createRoom( self, name ):
        new_room = Room( name, self )
        self.locations[ name ] = new_room
        self.loc_count += 1
        new_room.ID = self.loc_count
        self.loc_lut[ new_room.ID ] = name
        return new_room

    def createItemp( self, name ):
        new_item = Item( name, self )
        self.items[ name ] = new_item
        self.itm_count += 1
        new_item.ID = self.itm_count
        self.itm_lut[ new_room.ID ] = name
        return new_item


class Aobj( object ):
    def __init__( self, name, game ):
        self.name = name
        self.game = game
        self.noun = ""
        self.verb = ""
        self.syno = []
        self.ID   = -1
        # descriptions
        self.desc_short = ""
        self.desc_long  = ""


class Item( Aobj ):
    """ Item """
    def __init__( self, name, game ):
        super( Item, self ).__init__( name, game )
        self.location = -1
        self.actions = {}
        
    def moveTo( self, target ):
        new_loc  = self.game.locations[ target ]
        old_name = self.game.loc_lut[ self.location ]
        old_loc  = self.game.locations[ old_name ]
        old_loc.contents.remove( self )
        new_loc.contents.append( self )
        self.location = new_loc.ID

    def doAction( self, verb, other=None):
        pass


class Room( Aobj ):
    """ Room """
    def __init__( self, name ):
        super( Room, self ).__init__( name, game )
        self.navigation = []
        self.contents   = []


class Player( Aobj ):
    """ Player """
    def __init__( self, game ):
        super( Player, self ).__init__( "Player", game )

