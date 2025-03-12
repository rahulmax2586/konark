// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract MyContract {
    
    string public message;

    event MessageUpdated(string newMessage);

    constructor(string memory _message) {
        message = _message;
        emit MessageUpdated(_message);
    }

    function setMessage(string memory _message) public {
        message = _message;
        emit MessageUpdated(_message);
    }

    function getMessage() public view returns (string memory) {
        return message;
    }
}
