The following test cases outline the scenarios for testing the REST API:

Testcase No1:
| Step | Expected Result |
|:-----------: |:--------------:|
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
| Send API without including the animal_type and amount parameters| The value of type in response must be equal to "cat" and the length of response must be equal to 1|

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




