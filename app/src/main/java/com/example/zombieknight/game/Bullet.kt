package com.example.zombieknight.game

import kotlin.math.abs

class Bullet(
    center: Vec2,
    facingLeft: Boolean = false
) : Entity(Vec2(32f, 32f)) {

    private val vx: Float = if (facingLeft) -VELOCITY else VELOCITY
    private val startingX: Float
    var alive = true

    init {
        showTexture(Assets.image("player/slash.png"))
        flipH = facingLeft
        setTopLeft(center - Vec2(16f, 16f))
        startingX = rect.pos.x
    }

    fun update() {
        rect.pos.x += vx
        if (abs(rect.pos.x - startingX) > RANGE)
            alive = false
    }

    companion object {
        const val VELOCITY = 20f
        const val RANGE = 500f
    }


}