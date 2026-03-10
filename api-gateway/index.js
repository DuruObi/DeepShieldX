require("dotenv").config()
const express = require("express")
const cors = require("cors")

const v1 = require("./routes/v1")
const auth = require("./middleware/auth")

const app = express()

app.use(cors())
app.use(express.json())
app.use("/v1", auth, v1)

app.listen(8000, () => {
  console.log("API Gateway running on port 8000")
})
