package com.example.zombieknight.game

import com.example.zombieknight.game.Action.*

class Player(
    start: Vec2,
    private val platforms: List<Tile>,
    private val portals: List<Portal>,
    private val input: Input
) : Entity(Vec2(64f, 64f)) {

    // animations
    private val runFrames = loadFrames("player/run", "Run", 10)
    private val idleFrames = loadFrames("player/idle", "Idle", 10)
    private val jumpFrames = loadFrames("player/jump", "Jump", 10)
    private val attackFrames = loadFrames("player/attack", "Attack", 10)

    // sounds
    private val jumpSound = addSound("jump_sound")
    private val slashSound = addSound("slash_sound")
    private val portalSound = addSound("portal_sound")
    val hitSound = addSound("player_hit")

    // animation state
    private var animateJump = false
    private var animateFire = false
    var facingLeft = false

    // kinematics
    var pos: Vec2 = start.copy()
    var velocity = Vec2(0f, 0f)
    private var acceleration = Vec2(0f, GRAVITY)

    // player stuff
    var health = STARTING_HEALTH
    private val startingPos = start.copy()

    init {
        showTexture(idleFrames[0])
        setBottomLeft(pos)
    }

    fun update() {
        move()
        checkCollision()
        checkAnimation()
    }

    private fun move() {
        // handle inputs
        if (input.isPressed(MOVE_LEFT)) {
            acceleration.x = -HORIZONTAL_ACCELERATION
            facingLeft = true
            animate(runFrames, 0.5f)
        } else if (input.isPressed(MOVE_RIGHT)) {
            acceleration.x = HORIZONTAL_ACCELERATION
            facingLeft = false
            animate(runFrames, 0.5f)
        } else {
            animate(idleFrames, 0.5f)
        }

        flipH = facingLeft

        // friction
        acceleration.x -= velocity.x * HORIZONTAL_FRICTION
        velocity += acceleration
        pos += velocity + 0.5f * acceleration

        if (pos.x < 0) pos.x = WINDOW_WIDTH
        else if (pos.x > WINDOW_WIDTH) pos.x = 0f
        setBottomLeft(pos)
    }

    private fun platformHit() = platforms.firstOrNull { rect.intersects(it.rect) }

    private fun checkCollision() {
        // falling
        if (velocity.y > 0) {
            val t = platformHit()
            if (t != null){
                pos.y = t.rect.top + 1
                velocity.y = 0f
                setBottomLeft(pos)
            }
        }
        // jumping
        if (velocity.y < 0){
            if(platformHit() != null){
                velocity.y = 0f
                while(platformHit() != null){
                    pos.y += 1
                    setBottomLeft(pos)
                }
            }
        }
        // portals
        for(p in portals){
            if(rect.intersects(p.rect)){
                portalSound.play()
                pos.x = if (pos.x > WINDOW_WIDTH / 2) 86f else WINDOW_WIDTH - 150
                pos.y = if (pos.y > WINDOW_HEIGHT / 2) 64f else WINDOW_HEIGHT - 132
                setBottomLeft(pos)
                break
            }
        }
    }

    private fun checkAnimation() {
        if(animateJump){
            if(animate(jumpFrames, 0.1f)) animateJump = false
        }
        if(animateFire){
            if(animate(attackFrames, 0.25f)) animateFire = false
        }
    }

    fun jump() {
        if (platformHit() != null){
            jumpSound.play()
            velocity.y = - VERTICAL_JUMP_SPEED
            animateJump = true
        }
    }

    fun fire() : Bullet {
        slashSound.play()
        animateFire = true
        return Bullet(rect.center, facingLeft)
    }

    fun reset(){
        velocity = Vec2(0f, 0f)
        pos = startingPos.copy()
        setBottomLeft(pos)
    }

    companion object {
        const val HORIZONTAL_ACCELERATION = 2f
        const val HORIZONTAL_FRICTION = 0.15f
        const val GRAVITY = 0.8f
        const val VERTICAL_JUMP_SPEED = 18f
        const val STARTING_HEALTH = 100
    }

}
