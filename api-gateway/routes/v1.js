const FormData = require("form-data")
const express = require("express")
const axios = require("axios")
const multer = require("multer")

const router = express.Router()
const upload = multer()

const AI_ENGINE = "http://localhost:8500"

router.post("/voice/check", upload.single("audio"), async (req, res) => {
  try {
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

module.exports = router
