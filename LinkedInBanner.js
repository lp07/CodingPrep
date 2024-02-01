const life = 'full of challenges';

const handleChallenges = (thought) => {
    if (thought.content === 'I want to give up') {
        throw new Error('Not yet! Embrace the challenges and keep going!');
    } else {
        console.log('You are on the right path. Keep coding!');
    }
};

handleChallenges({ content: 'I want to give up' });
