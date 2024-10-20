## API Testing Overview

In this section, I describe the testing process for the API, which accepts two parameters: animal_type and amount.

  * Animal Types: The API supports four specific animal types: cat, dog, horse, and snail. The API provides specific responses only for these animals.
  * Amount Field: The amount parameter has a maximum limit of 500.


## Testing Approach

1. Initial Tests:

  * I began by running test cases without sending any parameters and by sending parameters with null values to observe the API's behavior in these scenarios.

2. Invalid Animal Type:

  * Next, I tested the API by sending an animal type that is not included in the list, such as "Lion", to evaluate how the API handles unexpected input.

3. Valid Animal Types:

  * I then sent requests for each of the listed animals to ensure the API returns the correct responses.

4. Amount Parameter Testing:

  * For the amount field, I tested the following boundary values:

     * 0 (minimum)
     * 1 (a normal value)
     * 500 (maximum limit)
     * 504 (exceeding the maximum limit)

  * Additionally, I included a normal value, such as 5, to verify the API’s correctness under standard conditions.

Through these tests, I aimed to ensure that the API handles both valid and invalid inputs correctly and adheres to the specified parameter constraints.

## Test Cases

Below are the specific test cases I executed for REST API testing:

Testcase No1:

| Step | Expected Result |
|:-----------:|--------------|
| Send an API request with the animal_type parameter set to "cat" and the amount parameter set to a random value, such as "2" | Response status code must be equal to 200 |


Testcase No2:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request without including the animal_type parameter, and set the amount parameter to a random value, such as "2" | The value of type in response must be equal to "cat"|

Testcase No3:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the animal_type parameter set to null and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "cat"|

Testcase No4:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the animal_type parameter set to an undefined value, such as "lion", and the amount parameter set to a random value, such as "2"| API response must be empty|

Testcase No5:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the animal_type parameter set to "cat" and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "cat"|

Testcase No6:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the animal_type parameter set to "dog" and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "dog"|

Testcase No7:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the animal_type parameter set to "snail" and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "snail"|

Testcase No8:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the animal_type parameter set to "horse" and the amount parameter set to a random value, such as "2"| The value of type in response must be equal to "horse"|

Testcase No9:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request without including the animal_type and amount parameters| The value of type in response must be equal to "cat" and the length of response must be equal to 1|

Testcase No10:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request without including the amount parameter, and set the animal_type parameter to a random value, such as "cat"| The length of the response must be equal to 1 |

Testcase No11:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the amount parameter set to "0" and the animal_type parameter set to a random value, such as "cat"| API response must be empty |

Testcase No12:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the amount parameter set to null and the animal_type parameter set to a random value, such as "cat"| The length of the response must be equal to 1|

Testcase No13:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the amount parameter set to "5" and the animal_type parameter set to a random value, such as "cat"| The length of the response must be equal to 5 |

Testcase No14:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the amount parameter set to the maximum valid value of "500" and the animal_type parameter set to a random value, such as "cat"| The length of the response must be equal to 500 |

Testcase No15:
| Step | Expected Result |
|:-----------: |:--------------:|
| Send an API request with the amount parameter set to a value exceeding the maximum limit, such as "504", and the animal_type parameter set to a random value, such as "cat"| You must receive this response from API: "Limited to 500 facts at a time" |




