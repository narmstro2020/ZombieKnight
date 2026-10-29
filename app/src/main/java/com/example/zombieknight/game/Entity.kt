package com.example.zombieknight.game

open class Entity(size: Vec2) {
    val rect = Rect(Vec2(0f, 0f), size)
    var texture: Texture? = null
    var flipH = false
    var currentSprite = 0f

    fun showTexture(texture: Texture){
        this.texture = texture
    }

    fun setTopLeft(pos : Vec2){
        rect.pos.x = pos.x
        rect.pos.y = pos.y
    }

    fun setBottomLeft(pos: Vec2){
        val newPos = pos - Vec2(0f, rect.pos.y)
        setTopLeft(newPos)
    }




}