// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var appstormapp_pb = require('./appstormapp_pb.js');

function serialize_appstorm_GenerateAppRequest(arg) {
  if (!(arg instanceof appstormapp_pb.GenerateAppRequest)) {
    throw new Error('Expected argument of type appstorm.GenerateAppRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_appstorm_GenerateAppRequest(buffer_arg) {
  return appstormapp_pb.GenerateAppRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_appstorm_GenerateAppResponse(arg) {
  if (!(arg instanceof appstormapp_pb.GenerateAppResponse)) {
    throw new Error('Expected argument of type appstorm.GenerateAppResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_appstorm_GenerateAppResponse(buffer_arg) {
  return appstormapp_pb.GenerateAppResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_appstorm_PublishNFTRequest(arg) {
  if (!(arg instanceof appstormapp_pb.PublishNFTRequest)) {
    throw new Error('Expected argument of type appstorm.PublishNFTRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_appstorm_PublishNFTRequest(buffer_arg) {
  return appstormapp_pb.PublishNFTRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_appstorm_PublishNFTResponse(arg) {
  if (!(arg instanceof appstormapp_pb.PublishNFTResponse)) {
    throw new Error('Expected argument of type appstorm.PublishNFTResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_appstorm_PublishNFTResponse(buffer_arg) {
  return appstormapp_pb.PublishNFTResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


// Define the gRPC service
var AppStormServiceService = exports.AppStormServiceService = {
  // RPC to generate an app
generateApp: {
    path: '/appstorm.AppStormService/GenerateApp',
    requestStream: false,
    responseStream: false,
    requestType: appstormapp_pb.GenerateAppRequest,
    responseType: appstormapp_pb.GenerateAppResponse,
    requestSerialize: serialize_appstorm_GenerateAppRequest,
    requestDeserialize: deserialize_appstorm_GenerateAppRequest,
    responseSerialize: serialize_appstorm_GenerateAppResponse,
    responseDeserialize: deserialize_appstorm_GenerateAppResponse,
  },
  // RPC to publish NFT (placeholder)
publishNFT: {
    path: '/appstorm.AppStormService/PublishNFT',
    requestStream: false,
    responseStream: false,
    requestType: appstormapp_pb.PublishNFTRequest,
    responseType: appstormapp_pb.PublishNFTResponse,
    requestSerialize: serialize_appstorm_PublishNFTRequest,
    requestDeserialize: deserialize_appstorm_PublishNFTRequest,
    responseSerialize: serialize_appstorm_PublishNFTResponse,
    responseDeserialize: deserialize_appstorm_PublishNFTResponse,
  },
};

exports.AppStormServiceClient = grpc.makeGenericClientConstructor(AppStormServiceService, 'AppStormService');
