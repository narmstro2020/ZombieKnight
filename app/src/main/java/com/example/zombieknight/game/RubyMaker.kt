package com.example.zombieknight.game

object RubyMaker :
    Entity(Vec2(64f, 64f)) {

    private val frames = loadTiles("ruby", 7)
    private val pos = Vec2(20 * 32f, 0f)

    init {
        showTexture(frames[0])
        setBottomLeft(pos)
    }

    fun update() {
        animate(frames, 0.25f)
    }



}