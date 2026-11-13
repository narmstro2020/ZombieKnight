package com.example.zombieknight.game

enum class Action {
    MOVE_LEFT,
    MOVE_RIGHT,
    JUMP,
    FIRE,
    ACCEPT
}

class Input {

    private val held = mutableSetOf<Action>()
    private val pressed = mutableSetOf<Action>()

    fun isPressed(action: Action) = action in held

    fun justPressed(action: Action) = action in pressed

    fun pressAction(action: Action) {
        if(action !in held) pressed.add(action)
        held.add(action)
    }

    fun releaseAction(action: Action) = held.remove(action)

    fun releaseAll() = held.clear()

    fun endTick() = pressed.clear()


}