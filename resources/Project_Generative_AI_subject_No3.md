# Development of a Voice Note Mobile App for Capturing Startup Ideas

**Course**: Generative AI  
**University**: Dauphine-PSL University

## Project Description

This project involves building a **mobile application** (Android or iOS) that allows users to quickly capture ideas by voice while on the go — whether biking, walking, or driving. The app records voice notes, transcribes them using speech-to-text, and then leverages an LLM to structure, enhance, and organize the raw ideas into actionable startup concepts.

The use case is simple: you're out for a run or commuting, and a great startup idea hits you. Instead of fumbling with a phone keyboard, you just tap and speak. The AI does the rest — transcribing, cleaning up, structuring, and even expanding on your idea.

#### USE CLAUDE CODE AS MUCH AS YOU CAN TO BE MORE PRODUCTIVE

## Objectives

1. **App Design:**
   - Design a minimal, distraction-free mobile interface optimized for one-handed and eyes-free use
   - Plan the user flow: record → transcribe → enhance → save
   - Choose your platform: Android (Kotlin/Java or React Native) or iOS (Swift or React Native)

2. **Core Features:**
   - **Voice Recording**: One-tap voice recording with a large, accessible button
   - **Speech-to-Text**: Transcribe the voice recording into text (using on-device or cloud-based STT)
   - **AI Enhancement**: Send the raw transcript to Claude's API to:
     - Clean up and structure the idea
     - Generate a title and summary
     - Suggest a potential target market and key features
     - Optionally: rate the idea's feasibility or novelty
   - **Idea Management**: Save, browse, edit, and delete past ideas
   - **Local Storage**: Store ideas locally on the device (SQLite or equivalent)

3. **Development:**
   - Implement the mobile app with a clean, intuitive UI
   - Integrate a speech-to-text engine (e.g., Android SpeechRecognizer, iOS Speech framework, or Whisper API)
   - Integrate Anthropic's Claude API for idea enhancement
   - Implement local data persistence

4. **Deployment:**
   - The app should be runnable on a real device or emulator
   - Provide an APK (Android) or TestFlight build (iOS), or a working emulator demo
   - Document setup and build instructions

## Requirements

1. Your project must:
   - Be a native or cross-platform mobile app (Android or iOS)
   - Include voice recording and speech-to-text functionality
   - Use Anthropic's Claude API to process and enhance voice notes
   - Store ideas locally on the device
   - Have a functional, user-friendly interface
   - Be properly documented

2. Technical requirements:
   - Use version control (Git)
   - Include a README with setup, build, and usage instructions
   - Include screenshots or a demo video of the app

## Getting Started

1. Your Anthropic API key will be provided by the instructor during the course.

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

#### Please only use `claude-haiku-3-5-20241022` (Claude 3.5 Haiku) to manage API costs.

2. Choose your platform and development framework:

| Platform | Framework Options | Language |
|----------|-------------------|----------|
| Android  | Native Android    | Kotlin or Java |
| iOS      | Native iOS        | Swift |
| Both     | React Native      | JavaScript/TypeScript |
| Both     | Flutter           | Dart |

3. Set up your mobile development environment:
   - **Android**: Install [Android Studio](https://developer.android.com/studio)
   - **iOS**: Install [Xcode](https://developer.apple.com/xcode/) (macOS only)
   - **React Native**: Follow the [React Native setup guide](https://reactnative.dev/docs/environment-setup)
   - **Flutter**: Follow the [Flutter setup guide](https://docs.flutter.dev/get-started/install)

4. Create a GitHub account if you don't have one

5. Fork the course repository: https://github.com/End2EndAI/Generative-AI-Module-Dauphine-2026

6. Create a new branch for your project and start developing

## Suggested Architecture

```
┌─────────────────────────────────────┐
│           Mobile App UI             │
│  ┌───────────┐  ┌───────────────┐   │
│  │  Record    │  │  Ideas List   │   │
│  │  Button    │  │  & Details    │   │
│  └─────┬─────┘  └───────────────┘   │
│        │                             │
│  ┌─────▼─────────────────────────┐   │
│  │   Speech-to-Text Engine       │   │
│  │   (on-device or cloud)        │   │
│  └─────┬─────────────────────────┘   │
│        │                             │
│  ┌─────▼─────────────────────────┐   │
│  │   Claude API (Anthropic)      │   │
│  │   - Structure the idea        │   │
│  │   - Generate title/summary    │   │
│  │   - Suggest target market     │   │
│  └─────┬─────────────────────────┘   │
│        │                             │
│  ┌─────▼─────────────────────────┐   │
│  │   Local Database (SQLite)     │   │
│  │   - Store enhanced ideas      │   │
│  └───────────────────────────────┘   │
└─────────────────────────────────────┘
```

## Suggested Prompt for Idea Enhancement

Here's an example of how to prompt Claude to enhance a raw voice note:

```python
import anthropic

client = anthropic.Anthropic()

raw_transcript = "so I was thinking about like an app that helps people find parking spots in the city using real-time data from sensors and maybe other drivers could share when they leave a spot"

message = client.messages.create(
    model="claude-haiku-3-5-20241022",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"""You are a startup idea analyst. A user just recorded a voice note with a startup idea.
The raw transcript is below. Please:
1. Give the idea a clear, catchy title
2. Write a clean 2-3 sentence summary of the idea
3. Identify the target market
4. List 3-4 key features the app would need
5. Rate the idea from 1-10 on novelty and feasibility

Raw transcript:
"{raw_transcript}"
"""
        }
    ]
)

print(message.content[0].text)
```

## Resources

1. [Anthropic API Documentation](https://docs.anthropic.com/en/docs/build-with-claude/overview)
2. [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
3. [Android Speech-to-Text](https://developer.android.com/reference/android/speech/SpeechRecognizer)
4. [iOS Speech Framework](https://developer.apple.com/documentation/speech)
5. [React Native Voice](https://github.com/react-native-voice/voice)
6. [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
