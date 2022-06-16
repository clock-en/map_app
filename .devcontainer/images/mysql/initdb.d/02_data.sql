USE map_app;

/*
name: 'test1'
email: 'test1@example.com'
password: 'test-1234'
*/
INSERT INTO users (name, email, password) VALUES (
    'test1',
    'test1@example.com',
    '$2b$12$9hO29GtfAY3xmv83yr3u7uMroqPStHQuPptNjm3Qu1Rb7UU9UB4Ga'
);

/*
name: '東京駅'
location: 35.68142354732969, 139.76709261114823
user_id: 1
*/
INSERT INTO spots (name, latitude, longitude, user_id) VALUES
('東京駅',35.68142354732969,139.76709261114823,1),
('皇居',35.685520571314576, 139.7529408938786,1);
