arg_list = argv();
lambda = str2double(arg_list{1});
sigma2 = str2double(arg_list{2});
file_X_train = arg_list{3};
file_y_train = arg_list{4};
file_X_test = arg_list{5};

%lambda = 2;
%sigma2 = 3;
%file_X_train = 'X_train.csv';
%file_y_train = 'y_train.csv';
%file_X_test = 'X_test.csv';

X = load(file_X_train);
y = load(file_y_train);
X_test = load(file_X_test);

% Part 1
d = size(X,2);
W_RR = pinv(lambda*eye(d) + X'*X)*X'*y;

wRR_outputfile = strcat('wRR_',num2str(lambda),'.csv');
csvwrite(wRR_outputfile, W_RR);

% Part 2
Sigma = pinv(lambda * eye(d) + 1/sigma2 *X'*X);
active = zeros(1,10);
m = size(X_test, 1);
for i=1:10
  maxSigma0 = 0;
  index = 0;
  % Select the x0 with max variance
  for j = 1:m
    if any(active == j)
      continue
    end
    x0 = X_test(j,:)';
    sigma0 =  x0' * Sigma * x0;
    if sigma0 > maxSigma0
      maxSigma0 = sigma0;
      index = j;
      x0_max = x0;
    end
  end  
  active(i) = index;
  % Update Sigma
  Sigma = pinv(pinv(Sigma) + 1/sigma2 * x0_max * x0_max');
end

active_outputfile = strcat('active_',num2str(lambda),'_',num2str(sigma2),'.csv');
csvwrite(active_outputfile, active);

