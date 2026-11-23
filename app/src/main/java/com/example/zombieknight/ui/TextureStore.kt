package com.example.zombieknight.ui

import androidx.compose.ui.graphics.ImageBitmap
import com.example.zombieknight.game.Texture

interface TextureStore {
    fun get(path: Texture) : ImageBitmap?

    fun preload(paths: List<Texture>)
}
