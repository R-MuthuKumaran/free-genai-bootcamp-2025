### Step 1: Set Up Your Development Environment

1. **Install Node.js**: Ensure you have Node.js installed on your machine. You can download it from [nodejs.org](https://nodejs.org/).

2. **Install Create React App**: This tool sets up a new React project with a good default configuration.
   ```bash
   npx create-react-app french-language-portal
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd french-language-portal
   ```

### Step 2: Install Required Dependencies

You may need additional libraries for routing, state management, and styling. Install them using npm or yarn:

```bash
npm install react-router-dom axios styled-components
```

- `react-router-dom`: For routing between different pages.
- `axios`: For making API calls.
- `styled-components`: For styling your components.

### Step 3: Project Structure

Create a directory structure that aligns with the specifications provided. Here’s a suggested structure:

```plaintext
french-language-portal/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/                # Reusable components
│   ├── pages/                     # Page components
│   │   ├── Dashboard.js
│   │   ├── StudyActivities.js
│   │   ├── StudyActivityShow.js
│   │   ├── Words.js
│   │   ├── WordShow.js
│   │   ├── Groups.js
│   │   ├── GroupShow.js
│   │   ├── StudySessions.js
│   │   ├── StudySessionShow.js
│   │   └── Settings.js
│   ├── App.js                     # Main app component
│   ├── index.js                   # Entry point
│   ├── api/                       # API calls
│   │   └── api.js
│   ├── styles/                    # Global styles
│   │   └── GlobalStyles.js
│   └── utils/                     # Utility functions
│       └── helpers.js
├── package.json
└── README.md
```

### Step 4: Create Basic Components

1. **App.js**: Set up routing in your main application file.
   ```javascript
   import React from 'react';
   import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
   import Dashboard from './pages/Dashboard';
   import StudyActivities from './pages/StudyActivities';
   import StudyActivityShow from './pages/StudyActivityShow';
   import Words from './pages/Words';
   import WordShow from './pages/WordShow';
   import Groups from './pages/Groups';
   import GroupShow from './pages/GroupShow';
   import StudySessions from './pages/StudySessions';
   import StudySessionShow from './pages/StudySessionShow';
   import Settings from './pages/Settings';

   const App = () => {
       return (
           <Router>
               <Switch>
                   <Route path="/dashboard" component={Dashboard} />
                   <Route path="/study_activities" component={StudyActivities} />
                   <Route path="/study_activities/:id" component={StudyActivityShow} />
                   <Route path="/words" component={Words} />
                   <Route path="/words/:id" component={WordShow} />
                   <Route path="/groups" component={Groups} />
                   <Route path="/groups/:id" component={GroupShow} />
                   <Route path="/study_sessions" component={StudySessions} />
                   <Route path="/study_sessions/:id" component={StudySessionShow} />
                   <Route path="/settings" component={Settings} />
                   <Route path="/" exact component={Dashboard} />
               </Switch>
           </Router>
       );
   };

   export default App;
   ```

2. **Create Page Components**: For each page (e.g., `Dashboard.js`, `Words.js`), create a functional component that fetches data from the API and displays it.

### Step 5: Implement API Calls

In the `api/api.js` file, create functions to interact with your backend API:

```javascript
import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Adjust based on your backend URL

export const getLastStudySession = () => axios.get(`${API_URL}/dashboard/last_study_session`);
export const getStudyProgress = () => axios.get(`${API_URL}/dashboard/study_progress`);
export const getWords = (page = 1) => axios.get(`${API_URL}/words?page=${page}`);
// Add more API functions as needed
```

### Step 6: Style Your Application

Use `styled-components` or any CSS framework (like Bootstrap or Tailwind CSS) to style your components according to the design goals specified.

### Step 7: Run Your Application

Start your development server to see your application in action:

```bash
npm start
```

### Step 8: Build for Production

When you're ready to deploy, build your application:

```bash
npm run build
```

This will create an optimized production build in the `build` directory.

### Conclusion

You now have a basic setup for your English to French language learning portal front-end project. You can expand upon this by adding more features, improving the UI, and integrating with your backend API.