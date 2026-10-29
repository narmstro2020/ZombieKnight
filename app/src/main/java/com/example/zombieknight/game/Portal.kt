package com.example.zombieknight.game

class Portal(
    pos: Vec2,
    color: String
) : Entity(Vec2(72f, 72f)) {

    init{
        currentSprite = 0F
        showTexture("")
        setBottomLeft(pos)
    }

    fun update(){

    }

}