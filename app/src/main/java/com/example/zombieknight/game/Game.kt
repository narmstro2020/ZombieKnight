package com.example.zombieknight.game

class Game(private val world: World, private val player: Player) {

    var score = 0

    var roundNumber = 1

    var frameCount = 0

    var roundTime = STARTING_ROUND_TIME

    var zombieCreationTime = STARTING_ZOMBIE_CREATION_TIME

    var paused = false
        private set

    var mainText = ""
        private set

    var subText = ""
        private set

    private var onResume: (() -> Unit)? = null

    companion object {
        const val STARTING_ROUND_TIME = 30
        const val STARTING_ZOMBIE_CREATION_TIME = 5
    }

}