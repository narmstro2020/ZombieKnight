package com.example.zombieknight.game

class Portal(
    pos: Vec2,
    color: String
) : Entity(Vec2(72f, 72f)) {

    private val frames = loadTiles("portals/$color", 22)

    init{
        currentSprite = frames.indices.random().toFloat()
        showTexture(frames[currentSprite.toInt()])
        setBottomLeft(pos)
    }

    fun update(){
        animate(frames, 0.2f)
    }

}