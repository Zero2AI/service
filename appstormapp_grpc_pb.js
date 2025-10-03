// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var appstormapp_pb = require('./appstormapp_pb.js');

function serialize_GenerateAppRequest(arg) {
  if (!(arg instanceof appstormapp_pb.GenerateAppRequest)) {
    throw new Error('Expected argument of type GenerateAppRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GenerateAppRequest(buffer_arg) {
  return appstormapp_pb.GenerateAppRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_GenerateAppResponse(arg) {
  if (!(arg instanceof appstormapp_pb.GenerateAppResponse)) {
    throw new Error('Expected argument of type GenerateAppResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GenerateAppResponse(buffer_arg) {
  return appstormapp_pb.GenerateAppResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_PublishNFTRequest(arg) {
  if (!(arg instanceof appstormapp_pb.PublishNFTRequest)) {
    throw new Error('Expected argument of type PublishNFTRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_PublishNFTRequest(buffer_arg) {
  return appstormapp_pb.PublishNFTRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_PublishNFTResponse(arg) {
  if (!(arg instanceof appstormapp_pb.PublishNFTResponse)) {
    throw new Error('Expected argument of type PublishNFTResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_PublishNFTResponse(buffer_arg) {
  return appstormapp_pb.PublishNFTResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


// package appstorm;
//
// Define the gRPC service
var appstormappService = exports.appstormappService = {
  // RPC to generate an app
generateApp: {
    path: '/appstormapp/GenerateApp',
    requestStream: false,
    responseStream: false,
    requestType: appstormapp_pb.GenerateAppRequest,
    responseType: appstormapp_pb.GenerateAppResponse,
    requestSerialize: serialize_GenerateAppRequest,
    requestDeserialize: deserialize_GenerateAppRequest,
    responseSerialize: serialize_GenerateAppResponse,
    responseDeserialize: deserialize_GenerateAppResponse,
  },
  // RPC to publish NFT (placeholder)
publishNFT: {
    path: '/appstormapp/PublishNFT',
    requestStream: false,
    responseStream: false,
    requestType: appstormapp_pb.PublishNFTRequest,
    responseType: appstormapp_pb.PublishNFTResponse,
    requestSerialize: serialize_PublishNFTRequest,
    requestDeserialize: deserialize_PublishNFTRequest,
    responseSerialize: serialize_PublishNFTResponse,
    responseDeserialize: deserialize_PublishNFTResponse,
  },
};

exports.appstormappClient = grpc.makeGenericClientConstructor(appstormappService, 'appstormapp');
