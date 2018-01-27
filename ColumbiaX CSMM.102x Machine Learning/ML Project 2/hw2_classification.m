arg_list = argv();
file_X_train = arg_list{1};
file_y_train = arg_list{2};
file_X_test = arg_list{3};

%file_X_train = 'X_train.csv';
%file_y_train = 'y_train.csv';
%file_X_test = 'X_test.csv';

X = load(file_X_train);
y = load(file_y_train);
X_test = load(file_X_test);
y = y + 1;

% Class priors
m = length(y);
K = max(y);
prob_y = zeros(1,K);
for i=1:m
  prob_y(y(i)) = prob_y(y(i)) + 1;
end
prob_y = prob_y / m;
%disp(prob_y);

% Class conditional density
d = size(X,2);
mu = cell(1,K);
sigma = cell(1,K);
for i=1:K
  X_i = X(y == i,:);
  mu{i} = mean(X_i);
  sigma{i} = cov(X_i,1); % Normalised by Ny instead of Ny - 1
end
%disp(mu);
%disp(sigma);

% Class posteriors
m_test = size(X_test,1);
prob_y_x = zeros(1,K);
for i=1:m_test
  x0 = X_test(i,:);
  for j=1:K
    prob_y_x(j) = prob_y(j) / sqrt(det(sigma{j})) * exp(-0.5*(x0-mu{j})*pinv(sigma{j})*(x0-mu{j})');
  end
  prob_x = sum(prob_y_x);
  prob_y_x = prob_y_x / prob_x;
  X_test_prob(i,:) = prob_y_x;
end
%disp(X_test_prob);

% Output
csvwrite('probs_test.csv', X_test_prob);
