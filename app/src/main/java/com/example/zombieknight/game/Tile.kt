package com.example.zombieknight.game

import com.example.zombieknight.game.Type.*

enum class Type {
    EMPTY,
    DIRT,
    GROUND,
    LEFT_PLATFORM,
    CENTER_PLATFORM,
    RIGHT_PLATFORM,
    RUBY_MAKER,
    GREEN_PORTAL,
    PURPLE_PORTAL,
    PLAYER;

    val isTile get() = this != EMPTY && ordinal <= RIGHT_PLATFORM.ordinal
}

class Tile(pos: Vec2, val type: Type) :
    Entity(Vec2(32f, 32f)) {

    val isPlatform get() = type != DIRT && type != EMPTY

    init {
        showTexture("")
        setTopLeft(pos)
    }

    companion object {
        val SIZE = Vec2(32f, 32f)
    }

}