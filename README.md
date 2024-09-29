# Multilanguage Invoice Extractor
This MultiLanguage Invoice Extractor application is built using Streamlit and Google Generative AI (Gemini 1.5 Flash model). The process involves uploading an invoice image, which is then analyzed to extract details based on both the image content and the user's query.

# Process Overview:
## 1. User Interaction:
The user is presented with an interface where they can:
  1. Enter a custom text prompt (query or question related to the invoice).
  2. Upload an invoice image in jpg, jpeg, or png format.

## 2. Image Upload and Display:
Once the user uploads an image, the application:
  1. Opens the image using the PIL library.
  2. Displays the uploaded image on the webpage with a caption.

## 3. Text Input for User's Custom Query:
The user can enter a text prompt, such as asking for specific details (e.g., total amount, due date) from the invoice image. This input serves as the user's query to be answered.

## 4. Data Preparation for AI Model:
The uploaded invoice image is processed into a format compatible with the Gemini AI model:
  1. The image file is converted into bytes and paired with its MIME type (file format).
  2. This allows the image to be understood and analyzed by the AI model.

## 5. Generating AI Response:
The application constructs a pre-defined input prompt, instructing the AI model to act as an invoice expert.
The app uses the Gemini 1.5 Flash model to analyze:
  1. The user’s text input.
  2. The uploaded invoice image.
  3. The pre-defined prompt.
  4. The Gemini AI model processes this data to generate a meaningful response, which could include invoice details, answers to specific questions, or a summary based on the invoice content.

## 6. Display of Results:
Once the AI generates the response, it is displayed on the page under the subheader "Invoice Analysis Result:" The user can see the AI's interpretation of the invoice, answering their custom query based on the image and input prompt.

# Key Features:
1. Multi-language Support: The application is designed to handle invoices in different languages since the Gemini model can extract and interpret text from images in multiple languages.
2. Real-time Feedback: Users can interactively upload images and submit queries, and the AI provides real-time feedback based on the invoice's content.
3. AI-based Analysis: By leveraging Generative AI, the application doesn't just perform simple text extraction but attempts to understand and answer complex questions based on the context of the invoice.

# Process Summary:
Upload Invoice → Convert to Bytes → Query via Input → Analyze Using AI → Return Detailed Information.
The process seamlessly combines text and image data, allowing for advanced invoice extraction and query answering using state-of-the-art AI models.

