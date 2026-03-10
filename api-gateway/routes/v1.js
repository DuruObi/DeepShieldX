const FormData = require("form-data")
const express = require("express")
const axios = require("axios")
const multer = require("multer")

const router = express.Router()
const upload = multer()

const AI_ENGINE = process.env.AI_ENGINE_URL || "http://localhost:8500"

router.post("/voice/check", upload.single("audio"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: "audio file is required" })
    }

    const formData = new FormData()
    formData.append("audio", req.file.buffer, "audio.wav")

    const response = await axios.post(
      `${AI_ENGINE}/v1/voice/check`,
      formData,
      { headers: formData.getHeaders() }
    )

    res.json(response.data)
  } catch (err) {
    res.status(500).json({ error: err.message })
  }
})

router.post("/message/scan", async (req, res) => {
  try {
    const response = await axios.post(
      `${AI_ENGINE}/v1/message/scan`,
      req.body
    )

    res.json(response.data)
  } catch (err) {
    res.status(500).json({ error: err.message })
  }
})

router.post("/video/check", upload.single("video"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: "video file is required" })
    }

    const formData = new FormData()
    formData.append("video", req.file.buffer, "video.mp4")

    const response = await axios.post(
      `${AI_ENGINE}/v1/video/check`,
      formData,
      { headers: formData.getHeaders() }
    )

    res.json(response.data)
  } catch (err) {
    res.status(500).json({ error: err.message })
  }
})

router.post("/url/inspect", async (req, res) => {
  try {
    const response = await axios.post(
      `${AI_ENGINE}/v1/url/inspect`,
      req.body
    )

    res.json(response.data)
  } catch (err) {
    res.status(500).json({ error: err.message })
  }
})

router.post("/image/check", upload.single("image"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: "image file is required" })
    }

    const formData = new FormData()
    formData.append("image", req.file.buffer, "image.jpg")

    const response = await axios.post(
      `${AI_ENGINE}/v1/image/check`,
      formData,
      { headers: formData.getHeaders() }
    )

    res.json(response.data)
  } catch (err) {
    res.status(500).json({ error: err.message })
  }
})

module.exports = router
