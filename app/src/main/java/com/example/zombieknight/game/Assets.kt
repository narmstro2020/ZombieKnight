package com.example.zombieknight.game

typealias Texture = String

interface Surface {
    fun drawImage(
        texture: Texture,
        rect: Rect,
        flipH: Boolean
    )
}

interface Sound {
    fun play()
    fun stop()
    fun pause()
    fun resume()
    val playing: Boolean
}

fun interface SoundLoader {
    fun load(path: String, loop: Boolean): Sound
}

class StubSound : Sound {
    private var started = false
    override fun play() {
        started = true
    }

    override fun stop() {
        started = false
    }

    override fun pause() {}
    override fun resume() {
        started = true
    }

    override val playing get() = started
}

object Assets {
    var soundLoader: SoundLoader = SoundLoader { _, _ -> StubSound() }

    private val NOT_A_RESOURCE_CHAR = Regex("[^a-z0-9]+")

    fun image(path: String): Texture {
        return path.removeSuffix(".png").lowercase().replace(NOT_A_RESOURCE_CHAR, "_").trim('_')
    }

    fun sound(name: String, loop: Boolean = false): Sound {
        return soundLoader.load("sounds/$name.wav", loop)
    }

    fun frames(folder: String, base: String, count: Int): List<Texture> {
        return (1..count).map { image("$folder/$base`_$it") }
    }

    fun tiles(folder: String, count: Int): List<Texture> =
        (0..<count).map { image("$folder/Tile_$it") }

}

