package com.example.zombieknight.game

class World(val input: Input){

    val tileMap = Array(ROWS){
        Array(COLS){Type.EMPTY}
    }

    val tiles = mutableListOf<Tile>()
    val platforms = mutableListOf<Tile>()
    val portals = mutableListOf<Portal>()
    val bullets = mutableListOf<Bullet>()
    val rubies = mutableListOf<Ruby>()
    lateinit var rubyMaker : RubyMaker
    // lateinit var player : Player
    // val game: Game

    private val background = Assets.image("background.png")

    init {

    }




    companion object{
        const val ROWS = 23
        const val COLS = 40
    }

}