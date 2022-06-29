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
INSERT INTO spots (name, description, latitude, longitude, user_id) VALUES
('東京駅', '全国各地の駅弁が購入できる',35.68147,139.76708,1),
('皇居', 'ランニングに最適！',35.68551, 139.75276,1);
