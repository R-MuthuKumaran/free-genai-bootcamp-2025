# English to French Language Learning Portal - Frontend Technical Specifications

## Design Goals
    - User-Friendly & Immersive: The UI should be intuitive, visually engaging, and offer an immersive learning experience.
    - Attractive Visuals: Incorporate high-quality images, interactive animations, and responsive layouts.
    - Consistent Theme: Provide a unified look across the application with options for light/dark modes and system default.

## Pages and Components

### Dashboard (/dashboard)

#### Purpose

Offers an overview of the learner’s progress.

#### Components

    - Last Study Session: Displays details of the most recent session (activity, time, correct vs. wrong summary) with a link to the relevant vocabulary group.
    - Study Progress: Shows total words studied (e.g. 3/124) and mastery progress.
    - Quick Stats: Displays success rate, total study sessions, active groups, and study streak.
    - Start Studying Button: Navigates to the study activities page.

#### API Endpoints

GET /api/dashboard/last_study_session
GET /api/dashboard/study_progress
GET /api/dashboard/quick_stats

### Study Activities Index (/study_activities)

#### Purpose

Lists all available study activities.

####  Components

    - Study Activity Card: Shows a thumbnail, activity name, and buttons for launching or viewing details.

#### API Endpoint

GET /api/study_activities

### Study Activity Show (/study_activities/:id)

#### Purpose

Provides detailed information about a selected study activity.
#### Components

    - Display the activity’s name, high-quality thumbnail, and description.
    - Launch Button: Initiates the study activity.
    - Paginated List: Shows past study sessions with details like start/end times and review item count.

#### API Endpoints

GET /api/study_activities/:id
GET /api/study_activities/:id/study_sessions

### Study Activity Launch (/study_activities/:id/launch)

#### Purpose

Facilitates launching a study activity.

#### Components

    - Launch Form: Includes a dropdown to select a vocabulary group.
    - Launch Now Button: Opens the activity in a new tab.

#### Behavior

On submission, redirect to the study session details page.

#### API Endpoint

POST /api/study_activities

## Words Index (/words)

#### Purpose

Displays all vocabulary words.

#### Components

    - Paginated Word List: Columns for French word, English translation, correct count, and wrong count.
    - Interactive Element: Clicking a French word navigates to its detailed view.

#### API Endpoint

GET /api/words

### Word Show (/words/:id)

#### Purpose

Provides detailed information on a specific word.

#### Components

    - Display the French word, English translation, and study statistics (correct and wrong counts).
    - Vocabulary Groups: Rendered as clickable tags leading to the group details page.

#### API Endpoint

GET /api/words/:id

### Word Groups Index (/groups)

#### Purpose

Lists all vocabulary groups.

#### Components

    - Paginated Group List: Columns for group name and word count.
    - Navigation: Clicking a group directs the user to the group show page.

#### API Endpoint

GET /api/groups

### Group Show (/groups/:id)

#### Purpose

Shows detailed information about a specific vocabulary group.

#### Components

    - Display the group name and statistics (e.g., total word count).
    - Paginated Lists: Reuse the words index component for words and the study sessions component for sessions.

#### API Endpoints

GET /api/groups/:id
GET /api/groups/:id/words
GET /api/groups/:id/study_sessions

### Study Sessions Index (/study_sessions)

#### Purpose

Provides an overview of all study sessions.

#### Components

    - Paginated List: Columns for session ID, activity name, group name, start time, end time, and review item count.
    - Navigation: Clicking on a session navigates to its details.

#### API Endpoint

GET /api/study_sessions

### Study Session Show (/study_sessions/:id)

#### Purpose

Displays detailed information about a selected study session.

#### Components

    - Session Details: Activity name, group name, start/end times, and number of review items.
    - Word Review Items List: Reuses the words index component in a paginated format.

#### API Endpoints

GET /api/study_sessions/:id
GET /api/study_sessions/:id/words

### Settings (/settings)

#### Purpose

Allows users to configure their portal experience.

#### Components

    - Theme Selection: Options for Light, Dark, and System Default.
    - Reset History Button: Deletes all study sessions and word review items.
    - Full Reset Button: Drops all tables and re-creates them with seed data.

#### API Endpoints

POST /api/reset_history
POST /api/full_reset

## Additional Frontend Considerations
 - Responsive Design: Ensure the portal works seamlessly across devices.
 - Smooth Animations & Transitions: Use subtle effects to enhance the immersive experience.
 - Accessibility: Follow best practices (e.g., ARIA labels, high contrast) to accommodate all users.
 - Performance Optimization: Leverage caching and minimize API calls to ensure fast load times.