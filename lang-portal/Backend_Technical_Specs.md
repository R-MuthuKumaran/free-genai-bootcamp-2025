# English to French Language Learning Portal - Backend Technical Specifications

## Business Goal
The portal aims to:

- Provide a comprehensive inventory of French vocabulary for English speakers.
- Act as a Learning Record Store (LRS) to track correct and incorrect answers during practice sessions.
- Serve as a unified launchpad to access various interactive learning activities.

## Technical Requirements

- Programming Language & Framework: Python with Django for rapid API development.
- Database: SQLite3 (for prototyping; migration to a more robust system can be considered later).
- API: RESTful endpoints returning JSON data.
 -User Model: Designed for a single-user experience (no authentication/authorization).
- Task Runner: Utilize Invoke for automating tasks like database initialization, migrations, and data seeding.

## Directory Structure
```text
french_portal/                     # Root project directory
├── manage.py                      # Django’s command-line utility
├── french_portal/                 # Django project configuration
│   ├── __init__.py
│   ├── settings.py                # Project settings (development, production, etc.)
│   ├── urls.py                    # Root URL configuration
│   ├── wsgi.py                    # WSGI application entry point
│   └── asgi.py                    # ASGI application entry point (if needed)
├── apps/                          # Custom Django applications
│   ├── dashboard/                 # Dashboard app (overview pages, stats, etc.)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py              # Models specific to dashboard (if any)
│   │   ├── views.py
│   │   ├── urls.py                # App-specific URL configuration
│   │   └── tests.py
│   ├── words/                     # Words app (vocabulary management)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   ├── groups/                    # Groups app (vocabulary categorization)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   ├── study_sessions/            # Study sessions app (tracking practice sessions)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   └── study_activities/          # Study activities app (launching and tracking exercises)
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── tests.py
├── db/                            # Database and seed data
│   ├── migrations/                # Django migration files
│   │   ├── __init__.py
│   │   └── ... (migration files)
│   └── seeds/                     # Seed data in JSON format for initial population
│       └── french_words_seed.json
├── tasks/                         # Invoke tasks for automation
│   ├── __init__.py
│   └── tasks.py                   # Tasks to initialize, migrate, and seed the database, etc.
└── requirements.txt               # Python package dependencies
```

## Database Schema
- words - stored vocabulary words
    - id (integer): Unique identifier.
    - french (string): The French word (with appropriate accents).
    - english (string): The English translation.
    - parts (json): Details such as part of speech or additional metadata.
- words_groups - join table for words and groups many-to-many
    - id (integer): Unique identifier.
    - word_id (integer): Foreign key referencing a word.
    - group_id (integer): Foreign key referencing a vocabulary group.
- groups - thematic groups of words
    - id (integer): Unique identifier.
    - name (string): Thematic group name (e.g., "Salutations de Base").
- study_sessions - records of study sessions grouping word_review_items
    - id (integer): Unique session identifier.
    - group_id (integer): Associated vocabulary group.
    - created_at (datetime): Timestamp marking the start of the session.
    - study_activity_id (integer): Linked study activity identifier.
- study_activities - a specific study activity, linking a study session to group
    - id (integer): Unique identifier.
    - study_session_id (integer): Associated study session.
    - group_id (integer): Associated vocabulary group.
    - created_at (datetime): Timestamp of creation.
- word_review_items - a record of word practice, determining if the word was correct or not
    - word_id (integer): Linked word identifier.
    - study_session_id (integer): Associated study session.
    - correct (boolean): Indicates whether the answer was correct.
    - created_at (datetime): Timestamp when the review occurred.

## API Endpoints

Dashboard Endpoints

### GET /api/dashboard/last_study_session

Returns details of the most recent study session.

#### JSON Response

```json
{
  "id": 111,
  "group_id": 222,
  "created_at": "2025-02-08T17:20:23-05:00",
  "study_activity_id": 777,
  "group_name": "Salutations"
}
```

### GET /api/dashboard/study_progress

Provides overall study progress metrics.

#### JSON Response

```json
{
  "total_words_studied": 30,
  "total_available_words": 324
}
```

### GET /api/dashboard/quick_stats

Returns quick statistics.

#### JSON Response

```json
{
  "success_rate": 75.0,
  "total_study_sessions": 6,
  "total_active_groups": 1,
  "study_streak_days": 2
}
```

Study Activities Endpoints

### GET /api/study_activities/:id

Retrieves detailed information about a specific study activity.

#### JSON Response

```json
{
  "id": 1,
  "name": "Vocabulary Quiz",
  "thumbnail_url": "https://demo.com/thumbnail.jpg",
  "description": "Practice your French vocabulary with interactive exercises"
}
```

### GET /api/study_activities/:id/study_sessions

Retrieves paginated study sessions for a study activity.

#### JSON Response

```json
{
  "items": [
    {
      "id": 123,
      "activity_name": "Vocabulary Quiz",
      "group_name": "Salutations",
      "start_time": "2025-02-08T17:20:23-05:00",
      "end_time": "2025-02-08T17:30:23-05:00",
      "review_items_count": 20
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5,
    "total_items": 100,
    "items_per_page": 20
  }
}
```

### POST /api/study_activities

Launches a new study activity.

#### Request Parameters:

group_id (integer)
study_activity_id (integer)

#### JSON Response

```json
{
  "id": 333,
  "group_id": 222
}
```

Words Endpoints

### GET /api/words

Returns a paginated list of French vocabulary words.

#### JSON Response

```json
{
  "items": [
    {
      "french": "bonjour",
      "english": "hello",
      "correct_count": 5,
      "wrong_count": 2
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5,
    "total_items": 500,
    "items_per_page": 100
  }
}
```

### GET /api/words/:id

Retrieves detailed information for a specific word.

#### JSON Response

```json
{
  "french": "bonjour",
  "english": "hello",
  "stats": {
    "correct_count": 5,
    "wrong_count": 2
  },
  "groups": [
    {
      "id": 1,
      "name": "Salutations"
    }
  ]
}
```

Groups Endpoints

### GET /api/groups

Returns a paginated list of vocabulary groups.

#### JSON Response

```json
{
  "items": [
    {
      "id": 1,
      "name": "Salutations",
      "word_count": 20
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 1,
    "total_items": 10,
    "items_per_page": 100
  }
}
```

### GET /api/groups/:id

Retrieves detailed information about a specific group.

#### JSON Response

```json
{
  "id": 1,
  "name": "Salutations",
  "stats": {
    "total_word_count": 20
  }
}
```

### GET /api/groups/:id/words

Returns a paginated list of words belonging to a group.

#### JSON Response

```json
{
  "items": [
    {
      "french": "bonjour",
      "english": "hello",
      "correct_count": 5,
      "wrong_count": 2
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 1,
    "total_items": 20,
    "items_per_page": 100
  }
}
```

### GET /api/groups/:id/study_sessions

Retrieves a paginated list of study sessions for the group.

#### JSON Response

```json
{
  "items": [
    {
      "id": 123,
      "activity_name": "Vocabulary Quiz",
      "group_name": "Salutations",
      "start_time": "2025-02-08T17:20:23-05:00",
      "end_time": "2025-02-08T17:30:23-05:00",
      "review_items_count": 20
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 1,
    "total_items": 5,
    "items_per_page": 100
  }
}
```

Study Sessions Endpoints

### GET /api/study_sessions

Returns a paginated list of all study sessions.

#### JSON Response

```json
{
  "items": [
    {
      "id": 123,
      "activity_name": "Vocabulary Quiz",
      "group_name": "Salutations",
      "start_time": "2025-02-08T17:20:23-05:00",
      "end_time": "2025-02-08T17:30:23-05:00",
      "review_items_count": 20
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5,
    "total_items": 100,
    "items_per_page": 100
  }
}
```

### GET /api/study_sessions/:id

Retrieves detailed information about a specific study session.

#### JSON Response

```json
{
  "id": 123,
  "activity_name": "Vocabulary Quiz",
  "group_name": "Salutations",
  "start_time": "2025-02-08T17:20:23-05:00",
  "end_time": "2025-02-08T17:30:23-05:00",
  "review_items_count": 20
}
```

### GET /api/study_sessions/:id/words

Returns a paginated list of word review items for the session.

#### JSON Response

```json
{
  "items": [
    {
      "french": "bonjour",
      "english": "hello",
      "correct_count": 5,
      "wrong_count": 2
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 1,
    "total_items": 20,
    "items_per_page": 100
  }
}
```

Settings Endpoints

### POST /api/reset_history

Resets study history by deleting all study sessions and word review items.

#### JSON Response

```json
{
  "success": true,
  "message": "Study history has been reset"
}
```

### POST /api/full_reset

Fully resets the system by dropping all tables and re-creating them with seed data.

#### JSON Response

```json
{
  "success": true,
  "message": "System has been fully reset"
}
```

Word Review Endpoint

### POST /api/study_sessions/:id/words/:word_id/review

Submits a word review result.

#### Request Params
- id (study_session_id) integer
- word_id integer
- correct boolean

#### Request Payload:

```json
{
  "correct": true
}
```

#### JSON Response

```json
{
  "success": true,
  "word_id": 1,
  "study_session_id": 123,
  "correct": true,
  "created_at": "2025-02-08T17:33:07-05:00"
}
```

## Task Runner Tasks

### Initialize Database 

Create the words.db SQLite database.

### Migrate Database 

Run SQL migration files (located in the migrations folder) in sequential order.

Example file names:
```sql
    0001_init.sql
    0002_create_words_table.sql
```

### Seed Data

Import and transform JSON seed files from the seeds folder into the database.

Example seed file format:
```json
[
  {
    "french": "payer",
    "english": "to pay"
  }
]
```