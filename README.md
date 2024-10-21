## API Testing Overview

In this section, I describe the testing process for the API, which accepts two parameters: animal_type and amount.

  * Animal Types: The API supports four specific animal types: cat, dog, horse, and snail. The API provides specific responses only for these animals.
  * Amount Field: The amount parameter has a maximum limit of 500.


## Testing Approach

**1. Initial Tests:**

  I began by running test cases without sending any parameters and by sending parameters with null values to observe the API's behavior in these scenarios.

**2. Invalid Animal Type:**

  Next, I tested the API by sending an animal type that is not included in the list, such as "Lion", to evaluate how the API handles unexpected input.

**3. Valid Animal Types:**

  I then sent requests for each of the valid animals to ensure the API returns the correct responses.

**4. Amount Parameter Testing:**

  For the amount field, I tested the following boundary values:

   * 0 (zero value)
   * 1 (minimum boundary value)
   * 5 (normal value)
   * 500 (maximum value)
   * 504 (exceeding the maximum limit)

Through these tests, I aimed to ensure that the API handles both valid and invalid inputs correctly and adheres to the specified parameter constraints.

## Modularized Variables

To enhance code readability and maintain a clear separation of concerns, I created a dedicated variables file, Rest_API_test_variable.py, to store common variables. This includes endpoints, valid animal lists, and other amounts used for testing purposes. This approach not only promotes cleaner code but also simplifies the process of updating and managing these values across the test suite.

## Running the Tests

 To execute the tests, simply run the following command from the project root:
  ```sh
  pytest Rest_API_test.py
  ```

## Test Cases

Below are the specific test cases I executed for REST API testing:

Testcase 1:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the animal_type parameter set to "cat" and the amount parameter set to a random value, such as "2" | Response status code must be equal to 200 |


Testcase 2:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request without including the animal_type parameter, and set the amount parameter to a random value, such as "2" | The value of type in response must be equal to "cat"|

Testcase 3:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the animal_type parameter set to null and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "cat"|

Testcase 4:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the animal_type parameter set to an undefined value, such as "lion", and the amount parameter set to a random value, such as "2"| API response must be empty|

Testcase 5:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the animal_type parameter set to "cat" and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "cat"|

Testcase 6:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the animal_type parameter set to "dog" and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "dog"|

Testcase 7:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the animal_type parameter set to "snail" and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "snail"|

Testcase 8:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the animal_type parameter set to "horse" and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "horse"|

Testcase 9:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request without including the animal_type and amount parameters| The value of type in response must be equal to "cat" and the length of response must be equal to 1|

Testcase 10:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request without including the amount parameter, and set the animal_type parameter to a random value, such as "cat"| The length of the response must be equal to 1 |

Testcase 11:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the amount parameter set to "0" and the animal_type parameter set to a random value, such as "cat"| API response must be empty |

Testcase 12:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the amount parameter set to null and the animal_type parameter set to a random value, such as "cat"| The length of the response must be equal to 1|

Testcase 13:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the amount parameter set to "5" and the animal_type parameter set to a random value, such as "cat"| The length of the response must be equal to 5 |

Testcase 14:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the amount parameter set to the maximum valid value of "500" and the animal_type parameter set to a random value, such as "cat"| The length of the response must be equal to 500 |

Testcase 15:
| Step        | Expected Result |
|-------------|-----------------|
| Send an API request with the amount parameter set to a value exceeding the maximum limit, such as "504", and the animal_type parameter set to a random value, such as "cat"| You must receive this response from API: "Limited to 500 facts at a time" |




