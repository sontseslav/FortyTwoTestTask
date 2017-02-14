var spa = angular.module('spa', ['ngRoute']).config(['$locationProvider', function($locationProvider) {
  $locationProvider.hashPrefix('');
}]);;
//route config
spa.config(['$routeProvider', function($routeProvider) {
	console.log('config entered');
	$routeProvider
	//description page - home
	.when('/',{
		templateUrl: 'description.html',
		controller: 'descriptionController',
		title: 'description'
	})
	//features page
	.when('/features', {
		templateUrl: 'features.html',
		controller: 'featuresController',
		title: 'features'
	})
	//author page
	.when('/author', {
		templateUrl: 'author.html',
		controller: 'authorController',
		title: 'author'
	})
	.otherwise({
        redirectTo: '/'
    });
}
]);

//controllers
/*
spa.controller('descriptionController', function($scope) {
	$scope.activeClass = 'description';
});

spa.controller('featuresController', function($scope) {
	$scope.titleSuffix = 'features';
});

spa.controller('authorController', function($scope) {
	$scope.titleSuffix = 'author';
});
*/
spa.run(['$location', '$rootScope', function($location, $rootScope, $scope) {
    $rootScope.$on('$routeChangeSuccess', function (event, current, previous) {
        // test for current route
        console.log('run entered');
        if(current.$$route) {
            // Set current page title 
            $rootScope.title = '42-test-sontseslav - ' + current.$$route.title;
            console.log('new root');
        }
    });
}]);